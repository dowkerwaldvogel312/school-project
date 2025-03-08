def random_python_code(n):
    code = []
    for _ in range(n):
        line = f"{random.choice(['', 'print(', ')']) + random.choice(['', ',']).join([str(random.randint(0, 10)) for _ in range(random.randint(0, 3))])}"
        code.append(line)
    return "\n".join(code)
