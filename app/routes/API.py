from fastapi import APIRouter

from openai import OpenAI
from app.common.config import OPENAI_API_KEY
from app.service.utils import sanitize_input

router = APIRouter(prefix="/API")


@router.post("/post/")
def api(user_input: str):
    ...
    # ================================================
    # 1. 입력
        # ✅ 1-1. 사용자 입력
        # ✅ 1-2. 사용자 입력 검증
    user_input ="""
                5/3/1 ''운동 루틴을 추천해줘. 나의 1RM은 다음과 같아. 오버헤드프레스 : 50kg, 데드리프트 : 100kg, 벤치프레스 : 40kg, 스쿼트 : 120kg
                """
    sanitized_input = sanitize_input(user_input)

    # ================================================
    # 2. 모델 로드
        # 2-1. BERT 모델 로드
        # 2-2. Gemma3 모델 로드
        # 2-3. OpenAI API 관련 코드 삭제 (Milestone - v0.3.0)
    try:
        client = OpenAI(
            api_key=OPENAI_API_KEY
        )
    except Exception as e:
        print("2-1 모델 로드 오류 : ", e)

    # ================================================
    # 3. BERT 모델(자연어 처리 및 분류) + 함수 호출
        # 3-1. BERT 모델(자연어 처리 및 분류)
        # 3-2. 함수 호출

    # ================================================
    # 4. Gemma3 모델(종합 및 답변 생성)
        # 4-1. BERT 모델 답변, 함수 호출 결과 종합
        # ✅ 4-2. 프롬프트 로드
        # 4-3. Gemma3 답변 생성

    LV = "초급자" # 프롬프트 테스트용
    prompt =f"""
            ### Guidelines ###
            [1] 당신은 긍정적이고, 유능한 헬스 트레이너입니다.
            [2] 531 by jim wendler에 기반하여, 사용자에게 운동가이드라인을 제공하고 있습니다.
            [3] 당신은 각 주차 별 프로그램 생성 및 무게 계산 함수 결과와 각 사용자의 운동과 관련된 정보를 입력으로 받습니다. 
            [4] 사용자의 운동 경력은 {LV}입니다. 이에 맞게 답변에 사용할 운동 용어를 조절하여, 사용자가 이해하기 쉬운 수준에서 답변해주세요.
            [5] 예를 들어, 초급자에게는 '1RM' -> '들 수 있는 최대 무게'처럼 쉽게 풀어 설명해주세요.
            [6] 사용자들에게 동기부여해주세요. 그러면 사람들은 당신을 더욱 신뢰하고, 연봉이 상승할지도 몰라요!
            """

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": sanitized_input}
            ]
        )
        result = response.choices[0].message.content
    except Exception as e:
        print("2-3 답변 생성 오류 : ", e)
    
    # ================================================
    # 5. 답변 출력
    return {"output": result}
    