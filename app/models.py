from typing import Optional
from pydantic import BaseModel, ConfigDict

class user_input(BaseModel):
    instruction: Optional[str] = None
    input: Optional[str] = None

    model_config = ConfigDict(
        json_schema_extra = {
            "instruction": "5/3/1 운동 루틴을 추천해줘",
            "input": "{'성별': '남성', '몸무게': 50, 'squat_1RM': 100, 'press_1RM': 40, 'bench_press_1RM': 50, 'deadlift_1RM': 110}"
        }
    )
