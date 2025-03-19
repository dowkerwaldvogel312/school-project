import random

def get_random_python_code():
    # Generate a random number between 1 and 5
    num = random.randint(1, 5)

    # Return a random Python code based on the number
    if num == 1:
        return "print('Hello World!')"
    elif num == 2:
        return "x = 5\ny = 6\nprint(x + y)"
    elif num == 3:
        return "for i in range(10):\n   print(i)"
    elif num == 4:
        return "while True:\n   print('Hello World!')"
    else:
        return "def my_function():\n   print('Hello World!')"
