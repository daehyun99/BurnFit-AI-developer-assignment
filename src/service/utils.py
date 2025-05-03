import os
import re

def sanitize_input(input_string):
    # Remove any characters that are not alphanumeric or spaces
    sanitized_string = re.sub(r'[^\w\s]', '', input_string)
    return sanitized_string