import asyncio
from fastapi import FastAPI, APIRouter, WebSocket, WebSocketDisconnect
from contextlib import asynccontextmanager
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
from apscheduler.schedulers.asyncio import AsyncIOScheduler

# Classe para gerenciar conexões WebSocket
class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: dict):
        for connection in self.active_connections:
            try:
                await connection.send_json(message)
            except:
                pass # Ignora desconexões durante broadcast

manager = ConnectionManager()
scheduler = AsyncIOScheduler() # Scheduler assíncrono

# Listener para eventos do APScheduler
def listener(event):
    if event.code == EVENT_JOB_EXECUTED:
        payload = {
            "type": "executed",
            "job_id": event.job_id,
            "run_time": str(event.scheduled_run_time)
        }
    elif event.code == EVENT_JOB_ERROR:
        payload = {
            "type": "error",
            "job_id": event.job_id,
            "exception": str(event.exception)
        }
    else:
        return
    # Broadcast via loop do FastAPI (use asyncio para não bloquear)
    asyncio.create_task(manager.broadcast(payload))

# Lifespan para iniciar/desligar o scheduler
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Inicie o scheduler e adicione listener
    scheduler.add_listener(listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
    scheduler.start()
    yield
    # Shutdown: Desligue o scheduler
    scheduler.shutdown()

app = FastAPI(lifespan=lifespan)

# Endpoint WebSocket para clientes se conectarem
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    try:
        await manager.connect(websocket)

    except WebSocketDisconnect:
        manager.disconnect(websocket)

router = APIRouter(prefix="/jobs", tags=["jobs"])

# Endpoint REST exemplo: Liste jobs
@router.get("/")
async def jobs():
    jobs = scheduler.get_jobs()
    return [j.__dict__() for j in jobs]

# Endpoint REST exemplo: Adicione um job
@router.post("/")
async def create():
    def task():
        print(f"Task")
    
    scheduler.add_job(task, 'interval', seconds=10, id='my_job')
    return {"message": "Job adicionado"}