from transformers import AutoTokenizer, Gemma3ForCausalLM
from transformers import AlbertTokenizer, AlbertForMaskedLM
import torch

from app.common.config import HUGGING_FACE_TOKEN

from huggingface_hub import login

login(f"{HUGGING_FACE_TOKEN}")

def load_Gemma3():
    """
    
    """
    model_id = "google/gemma-3-1b-it"
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = Gemma3ForCausalLM.from_pretrained(
        model_id,
        torch_dtype=torch.bfloat16,
        # device_map="auto",
        )
    return model, tokenizer

def load_ALBert():
    """
    
    """
    model_id = "albert-base-v2"
    tokenizer = AlbertTokenizer.from_pretrained(model_id)
    model = AlbertForMaskedLM.from_pretrained(
        model_id,
        torch_dtype=torch.bfloat16,
        # device_map="auto",
        )
    return model, tokenizer