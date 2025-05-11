from fastapi import APIRouter

from app.service.utils import sanitize_input
from app.models import user_input

from app.service.llms import sampler

router = APIRouter(prefix="/API")


@router.post("/post/")
def api(user_input: user_input):
    """
    `531 프로그램 루틴 추천`
    :param user_input:
    :return output:
    """
    # ================================================
    # 1. 입력
        # ✅ 1-1. 사용자 입력
        # ✅ 1-2. 사용자 입력 검증
    try:
        if user_input:
            input = user_input.input
            instruction = user_input.instruction

            instruction = sanitize_input(instruction)

            prompt = f"""{instruction} {input}"""
        else:
            return ["🛑 사용자 입력 오류 : User input is None"]
    except Exception as e:
        return ["🛑 사용자 입력 오류 : ", str(e)]


    # ================================================
    # Gemma3 답변 생성
    try:
        result = sampler.chat(prompt)
    except Exception as e:
        return ["🛑 Gemma3 답변 생성 오류 : ", str(e)]
    
    # ================================================
    # 답변 출력
    return {"output": str(result)}
    