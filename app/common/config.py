from os import path
import os

base_dir = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))

os.environ["XLA_PYTHON_CLIENT_MEM_FRACTION"]="1.00"

model_path = ""