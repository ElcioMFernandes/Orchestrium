import os, uuid
from pathlib import Path
from fastapi import APIRouter, HTTPException

from ..core.scheduler import scheduler
from ..utils.serialize import serialize

router = APIRouter(tags=["tasks"], prefix="/tasks")

@router.get("/")
async def get_tasks():
    """Get all tasks"""
    try:
        directory = Path(__file__).parent.parent / "tasks"

        if not os.path.exists(directory):
            os.makedirs(directory)

        files = [f for f in os.listdir(directory) if f.endswith(".py") and f != "__init__.py"]

        return {"tasks": files}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{id}")
async def get_task(id: str):
    """Get a specific task by ID"""
    try:
        file = Path(__file__).parent.parent / "tasks" / f"{id}.py"

        if not file.exists():
            raise HTTPException(status_code=404, detail=f"Task {id} not found")

        with open(file, "r") as file:
            content = file.read()

        return {"id": id, "content": content}

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/")
async def create_task(content: str):
    """Create a new task"""
    try:
        id = str(uuid.uuid4())

        file = Path(__file__).parent.parent / "tasks" / f"{id}.py"

        with open(file, "w") as file:
            file.write(content)

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{id}")
async def delete_task(id: str):
    """Delete a task"""
    try:
        file = Path(__file__).parent.parent / "tasks" / f"{id}.py"

        if not file.exists():
            raise HTTPException(status_code=404, detail=f"Task {id} not found")

        os.remove(file)

        return {"detail": f"Task {id} removed successfully"}

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.put("/{id}")
async def update_task(id: str, content: str):
    """Update an existing task"""
    try:
        file = Path(__file__).parent.parent / "tasks" / f"{id}.py"

        if not file.exists():
            raise HTTPException(status_code=404, detail=f"Task {id} not found")

        with open(file, "w") as file:
            file.write(content)

        return {"detail": f"Task {id} updated successfully"}

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))