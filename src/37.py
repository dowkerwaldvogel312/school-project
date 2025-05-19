def calculate_sum(numbers):
    """
    Calculate the sum of a list of numbers.
    
    Args:
    numbers: A list of integers or floats.
    
    Returns:
    The sum of the numbers as an integer.
    """
    total = 0
    for num in numbers:
        total += num
    return total

# Example usage
numbers = [1, 2, 3, 4, 5]
result = calculate_sum(numbers)
print("The sum is:", result)
