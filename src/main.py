from openai import OpenAI
from common.config import OPENAI_API_KEY




# ================================================
# 1. 사용자 입력
# user_input = input()
user_input = "5/3/1 운동 루틴을 추천해줘. 나의 1RM은 다음과 같아. 오버헤드프레스 : 50kg, 데드리프트 : 100kg, 벤치프레스 : 40kg, 스쿼트 : 120kg"


# ================================================
# 2-1. 모델 로드
client = OpenAI(
    api_key=OPENAI_API_KEY
)

# 2-2. 프롬프트 로드
prompt = """당신은 유능한 헬스 트레이너입니다. 사용자의 요구사항에 따라 적절한 프로그램을 제시하세요."""

# 2-3. 답변 생성
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": prompt},
        {"role": "user", "content": user_input}
    ]
)
result = response.choices[0].message.content

# ================================================
# 3. 답변 출력
print("test : ", result)