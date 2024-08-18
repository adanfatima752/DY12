class DivisionByZeroError(Exception):
    pass

def divide_and_round(a, b, precision):
    if not isinstance(a, (int, float)):
        raise ValueError("The first input must be a numeric value.")
    if not isinstance(b, (int, float)):
        raise ValueError("The second input must be a numeric value.")
    if not isinstance(precision, int) or precision < 0:
        raise ValueError("Precision must be a non-negative integer.")
    
    if b == 0:
        raise DivisionByZeroError("Division by zero is not allowed.")
    
    result = a / b
    return round(result, precision)
try:
    result = divide_and_round(10, 3, 2)
    print("Result:", result)
except (DivisionByZeroError, ValueError) as e:
    print(e)

try:
    result = divide_and_round(10, 0, 2)
    print("Result:", result)
except (DivisionByZeroError, ValueError) as e:
    print(e)

try:
    result = divide_and_round(10, 3, -1)
    print("Result:", result)
except (DivisionByZeroError, ValueError) as e:
    print(e)
