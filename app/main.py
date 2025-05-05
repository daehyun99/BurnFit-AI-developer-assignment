import uvicorn
from fastapi import FastAPI

from app.routes import API

from app.service import llms

def create_app():
    """
    앱 함수 실행
    :return:
    """
    app = FastAPI()

    gemma3, gemma3_tokenizer = llms.load_Gemma3()
    albert, albert_tokenizer = llms.load_ALBert()

    app.include_router(API.router, tags=["API"])    
    return app

app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)