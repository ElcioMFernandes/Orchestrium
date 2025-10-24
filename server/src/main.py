from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from.routes import tasks

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
    allow_credentials=True,
)

app.include_router(tasks.router)