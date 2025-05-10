from dotenv import load_dotenv
from os import getenv, path, environ

base_dir = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))

load_dotenv()

OPENAI_API_KEY = getenv("OPENAI_API_KEY")
HUGGING_FACE_TOKEN = getenv("HUGGING_FACE_TOKEN")

model_path = path.join(base_dir, "app", "models")