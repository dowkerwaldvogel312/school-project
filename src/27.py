def fibonacci_sequence(n):
    """
    Calculate and print the Fibonacci sequence up to n terms.
    
    Parameters:
        n (int): The number of terms in the Fibonacci sequence.
        
    Returns:
        None
    """
    a, b = 0, 1
    while a < n:
        print(a)
        a, b = b, a + b

# Example usage:
fibonacci_sequence(10)

