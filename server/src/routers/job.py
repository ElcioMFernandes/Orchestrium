from fastapi import APIRouter

router = APIRouter(
    tags=["jobs"],
    prefix="/jobs"
)

@router.get("/")
async def read():
    return {"message": "List of jobs"}