import random

def generate_random_string(length):
    """
    Generate a random string of specified length.
    
    Parameters:
    - length: The length of the generated string.
    
    Returns:
    - A random string of the given length.
    """
    return ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789', k=length))

print(generate_random_string(10))
