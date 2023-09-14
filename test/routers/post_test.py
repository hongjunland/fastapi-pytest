from fastapi import Response
from fastapi.testclient import TestClient
from app.main import create_app
from app.routers.post import RequestModel

app = create_app()
client = TestClient(app)

def test_get_items():
    response = client.get("/posts")
    assert response.status_code == 200
    assert response.json() == [{"name": "item1"}, {"name": "item2"}]

def test_get_item_valid_id():
    response = client.get("/posts/1")
    assert response.status_code == 200
    assert response.json() == {"name": "item1", "id": 1}

def test_get_item_invalid_id():
    response = client.get("/posts/abc")
    assert response.status_code == 422  # 유효하지 않은 요청 데이터

def test_post_item_valid_id():
    dummy_request = RequestModel(item_id='zxczxc', item_name='zxczxcxzczx').model_dump()
    # dummy_request = {"item_id": 'zxczxc', 'item_name': 'zxczxczxc'}
    print(dummy_request)
    response = client.post("/posts", json=dummy_request)
    print(response)
    print(response.headers)
    print(response.status_code)
    assert response.status_code == 200