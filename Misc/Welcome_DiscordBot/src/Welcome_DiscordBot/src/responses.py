import random
import string

def generate_flag():
    digits_part = ''.join(random.choices(string.digits, k=10))
    chars_part = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    return f"GrizzCTF{{{digits_part}{chars_part}}}"

