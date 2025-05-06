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

## 커밋 타입
Feat : 기능 개발
Fix : 버그 수정
Docs : 문서 작성
Prompt : 프롬프트 개선
Data : 데이터 수집, 처리, 분석
Model : AI 모델 학습
Deploy : 배포 관련