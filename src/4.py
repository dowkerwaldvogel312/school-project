import random

def get_random_code():
    return str(random.randint(100000, 999999))

print(get_random_code())
