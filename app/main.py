import uvicorn
from api.api_v1.api import api_router
from db.base import Base, engine
from fastapi import FastAPI


def create_app() -> FastAPI:
    """ app 변수 생성 및 초기값 설정 """

    
    _app = FastAPI(
        title="fastapi-pytest",
        description="fastapi 테스트 코드 연습장",
        version="1.0.0",
    )
    Base.metadata.create_all(bind=engine)
    _app.include_router(api_router, prefix='/api/v1')
    return _app


app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)          
 