 import random
 
def get_random_code(length):
    char_pool = 'abcdefghijklmnopqrstuvwxyz'
    code = ''
    for _ in range(length):
        code += random.choice(char_pool)
    return code