from fastapi import APIRouter

router = APIRouter(
    tags=["triggers"],
    prefix="/triggers"
)

@router.get("/")
async def read():
    return {"message": "List of triggers"}