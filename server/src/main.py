from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import job, task, triggers

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

app.include_router(job.router)
app.include_router(task.router)
app.include_router(triggers.router)