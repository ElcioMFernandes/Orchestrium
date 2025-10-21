from fastapi import APIRouter, HTTPException

from ..core.scheduler import scheduler
from ..utils.serialize import serialize

router = APIRouter(tags=["jobs"], prefix="/jobs")

@router.get("/")
async def get_jobs():
    """Get all scheduled jobs"""
    try:
        jobs = scheduler.get_jobs()
        return [serialize(job) for job in jobs]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{id}")
async def get_job(id: str):
    """Get a specific job by ID"""
    try: 
        job = scheduler.get_job(id)

        if not job:
            raise HTTPException(status_code=404, detail=f"Job {id} not found")

        return serialize(job)

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/")
async def create_job(task):
    """Create a new scheduled job"""
    try:
        job = scheduler.add_job(task,  'interval',  seconds=10)

        if not job:
            raise HTTPException(status_code=400, detail="Job could not be created")

        return serialize(job)

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{id}")
async def delete_job(id: str):
    """Delete a scheduled job"""
    try:
        job = scheduler.get_job(id)

        if not job:
            raise HTTPException(status_code=404, detail=f"Job {id} not found")

        scheduler.remove_job(id)

        return {"detail": f"Job {id} removed successfully"}

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.put("/{id}/stop")
async def stop_job(id: str):
    """Stop a scheduled job"""
    try:
        job = scheduler.get_job(id)

        if not job:
            raise HTTPException(status_code=404, detail=f"Job {id} not found")

        job.pause()

        return {"detail": f"Job {id} stopped successfully"}

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.put("/{id}/resume")
async def resume_job(id: str):
    """Resume a scheduled job"""
    try:
        job = scheduler.get_job(id)

        if not job:
            raise HTTPException(status_code=404, detail=f"Job {id} not found")

        job.resume()

        return {"detail": f"Job {id} resumed successfully"}

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))