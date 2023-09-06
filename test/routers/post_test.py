from fastapi.testclient import TestClient
from app.main import create_app

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
