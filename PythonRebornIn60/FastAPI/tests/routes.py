from fastapi import APIRouter

router = APIRouter(prefix="/route")

@router.get("/item/{item_id}")
async def read_item(item_id: int):
    return {"Item 1": item_id}