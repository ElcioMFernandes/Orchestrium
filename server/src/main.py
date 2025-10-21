from fastapi import FastAPI
from contextlib import asynccontextmanager

from .routes import jobs, tasks
from .core.scheduler import scheduler

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Start the scheduler when the app starts
    scheduler.start()

    # Yield the app to the caller for use in routes
    yield

    # Shutdown the scheduler when the app stops
    scheduler.shutdown()

# Create FastAPI app with lifespan context
app = FastAPI(lifespan=lifespan)

app.include_router(jobs.router)
app.include_router(tasks.router)