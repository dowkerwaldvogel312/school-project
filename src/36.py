import random

def generate_random_string(length):
    """
    Generates a random string of specified length.
    
    Parameters:
    - length: An integer representing the desired length of the generated string.

    Example usage:
    >>> print(generate_random_string(5))
    "ABCDEFGH"
    """
    # Ensure the input is valid
    if not isinstance(length, int) or length < 0:
        raise ValueError("Length must be a non-negative integer.")
    
    # Generate a random string of given length
    return ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(length))

# Example usage: print(generate_random_string(5))
