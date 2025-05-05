# 실행
## 환경변수 설정
### .env
```sh
OPENAI_API_KEY=""
HUGGING_FACE_TOKEN=""
```

## 빠른 실행
```sh
pip install -r requirements.txt

uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```