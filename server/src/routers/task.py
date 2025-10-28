from typing import Optional
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

class CreateTaskRequest(BaseModel):
    name: str
    content: str

class UpdateTaskRequest(BaseModel):
    name: Optional[str] = None
    content: Optional[str] = None

TASKS = []

router = APIRouter(tags=["tasks"], prefix="/tasks")

@router.get("/")
async def get_tasks():
    """List of tasks"""
    return TASKS

@router.get("/{id}")
async def get_task(id: str):
    """Get a task"""
    for task in TASKS:
        if task["id"] == id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@router.post("/")
async def create_task(request: CreateTaskRequest):
    """Create a new task"""
    task = {
        "id": str(len(TASKS) + 1),
        "name": request.name,
        "content": request.content
    }
    TASKS.append(task)
    return task

@router.put("/{id}")
async def update_task(id: str, request: UpdateTaskRequest):
    """Update a task"""
    for task in TASKS:
        if task["id"] == id:
            if request.name is not None:
                task["name"] = request.name
            if request.content is not None:
                task["content"] = request.content
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@router.delete("/{id}")
async def delete_task(id: str):
    """Delete a task"""
    for index, task in enumerate(TASKS):
        if task["id"] == id:
            del TASKS[index]
            return {"detail": f"Task {id} removed successfully"}
    raise HTTPException(status_code=404, detail="Task not found")
