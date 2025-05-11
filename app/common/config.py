from os import path
import os
from dotenv import load_dotenv

load_dotenv()

base_dir = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))

os.environ["XLA_PYTHON_CLIENT_MEM_FRACTION"]="1.00"

GEMMA_MODEL_PATH = load_dotenv("GEMMA_MODEL_PATH", "/content/drive/MyDrive/05_[공유파일]/Burnfit-model/Gemma3-lora6")