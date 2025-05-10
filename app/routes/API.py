from fastapi import APIRouter

from app.service.utils import sanitize_input
from app.models import user_input

from app.service.llms import sampler

router = APIRouter(prefix="/API")


@router.post("/post/")
def api(user_input: user_input):
    ...
    # ================================================
    # 1. 입력
        # ✅ 1-1. 사용자 입력
        # ✅ 1-2. 사용자 입력 검증
    input = user_input.input
    instruction = user_input.instruction

    instruction = sanitize_input(instruction)

    prompt = f"""{instruction} {input}"""


    # ================================================
    # Gemma3 답변 생성
    sampler.chat(prompt)

    try:
        ...
        result = ""
    except Exception as e:
        print("2-3 답변 생성 오류 : ", e)
    
    # ================================================
    # 답변 출력
    return {"output": result}
    