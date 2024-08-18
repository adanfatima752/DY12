class NotANumberError(Exception):
    pass

def sum_two_numbers(a, b):
    if not isinstance(a, (int, float)):
        raise NotANumberError(f"Input {a} is not a number.")
    if not isinstance(b, (int, float)):
        raise NotANumberError(f"Input {b} is not a number.")
    return a + b
try:
    result = sum_two_numbers(10, 20)
    print("Sum:", result)
except NotANumberError as e:
    print(e)

try:
    result = sum_two_numbers(10, "abc")
    print("Sum:", result)
except NotANumberError as e:
    print(e)
