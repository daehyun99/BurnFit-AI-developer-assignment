import os
import re

def sanitize_input(input_string):
    """
    사용자 입력 검증
    """
    sanitized_string = re.sub(r'[^\w\s]', '', input_string)
    return sanitized_string