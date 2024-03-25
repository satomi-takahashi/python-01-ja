def add(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    else:
        return "bad input"

def subtract(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a - b
    else:
        return "bad input"

def multiply(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a * b
    else:
        return "bad input"

def divide(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"
    else:
        return "bad input"
