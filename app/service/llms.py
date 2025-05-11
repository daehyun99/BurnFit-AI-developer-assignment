from kauldron import kd
from gemma import gm
from gemma import peft

from app.common.config import GEMMA_MODEL_PATH

def load_Gemma3(model_path= GEMMA_MODEL_PATH):
    """
    Gemma3-1B 모델 로드
    """
    model = gm.nn.LoRA(
        rank=4,
        model=gm.nn.Gemma3_1B(tokens="batch.input"),
    )
    params = gm.ckpts.load_params(model_path)
    
    tokenizer = gm.text.Gemma3Tokenizer()

    sampler = gm.text.ChatSampler(
        model=model,
        params=params,
        tokenizer=tokenizer
    )
    return sampler

sampler = load_Gemma3()