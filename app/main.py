from fastapi import FastAPI
import uvicorn
from routers.post import post_router


def create_app() -> FastAPI:
    """ app 변수 생성 및 초기값 설정 """

    
    _app = FastAPI(
        title="fastapi-pytest",
        description="fastapi 테스트 코드 연습장",
        version="1.0.0",
    )
    _app.include_router(post_router, prefix="/posts", tags=["게시판 - posts"])
    return _app


app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)          
 