import random

def get_random_code():
    code = "".join(random.choice("0123456789abcdef") for _ in range(8))
    return code
