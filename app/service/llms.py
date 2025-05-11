from kauldron import kd
from gemma import gm
from gemma import peft


def load_Gemma3(path = "/content/drive/MyDrive/05_[공유파일]/Burnfit-model/Gemma3-lora6"):
    """
    path 
    """
    model = gm.nn.LoRA(
        rank=4,
        model=gm.nn.Gemma3_1B(tokens="batch.input"),
    )
    params = gm.ckpts.load_params(path)
    
    tokenizer = gm.text.Gemma3Tokenizer()

    sampler = gm.text.ChatSampler(
        model=model,
        params=params,
        tokenizer=tokenizer
    )
    return sampler

sampler = load_Gemma3()