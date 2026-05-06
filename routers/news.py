from fastapi import APIRouter

router = APIRouter(prefix="/api/news", tags=["news"])

@router.get("/categories")
async def get_categories(skip: int = 0, limit: int = 10):
    return {
        "code": 200,
        "msg": "success",
        "data": "news list"
    }
