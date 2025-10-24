from typing import Optional
from fastapi import APIRouter, HTTPException, Depends
from ..config import MONGO
from ..repos.task import MongoDBTaskRepository
from ..models.task import Task

router = APIRouter(tags=["tasks"], prefix="/tasks")

def get_task_repository():
    """Injeção de dependência para o repositório."""
    return MongoDBTaskRepository(MONGO)

@router.get("/")
async def get_tasks(repository: MongoDBTaskRepository = Depends(get_task_repository)):
    """Get all tasks"""
    try:
        tasks = await repository.list()
        return {"tasks": [task.dict() for task in tasks]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{id}")
async def get_task(id: str, repository: MongoDBTaskRepository = Depends(get_task_repository)):
    """Get a specific task by ID"""
    try:
        task = await repository.read(id)
        return {"id": task.id, "content": task.content, "name": task.name}
    except Exception as e:
        if "not found" in str(e).lower():
            raise HTTPException(status_code=404, detail=str(e))
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/")
async def create_task(content: str, name: str, repository: MongoDBTaskRepository = Depends(get_task_repository)):
    """Create a new task"""
    try:
        task = Task.create(content, name)
        created = await repository.create(task)
        return {"id": created.id, "name": created.name}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{id}")
async def update_task(id: str, content: str, name: Optional[str] = None, repository: MongoDBTaskRepository = Depends(get_task_repository)):
    """Update an existing task"""
    try:
        existing = await repository.read(id)

        existing.content = content
        if name is not None:
            existing.name = name

        updated_task = await repository.update(id, existing)
        return {"detail": f"Task {id} updated successfully", "task": updated_task.dict()}
    except Exception as e:
        if "not found" in str(e).lower():
            raise HTTPException(status_code=404, detail=str(e))
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{id}")
async def delete_task(id: str, repository: MongoDBTaskRepository = Depends(get_task_repository)):
    """Delete a task"""
    try:
        await repository.delete(id)
        return {"detail": f"Task {id} removed successfully"}
    except Exception as e:
        if "not found" in str(e).lower():
            raise HTTPException(status_code=404, detail=str(e))
        raise HTTPException(status_code=500, detail=str(e))