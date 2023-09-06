from fastapi import APIRouter

post_router = APIRouter()

@post_router.get("")
def get_items():
    return [{"name": "item1"}, {"name": "item2"}]


@post_router.get("/{item_id}")
def get_item(item_id: int):
    return {"name": "item1", "id": item_id}