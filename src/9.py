import random

def get_random_number(n):
    return random.randint(1, n)

def get_random_string(length):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for i in range(length):
        result += alphabet[random.randint(0, len(alphabet) - 1)]
    return result

def get_random_list(n):
    result = []
    for i in range(n):
        result.append(random.randint(1, n))
    return result
