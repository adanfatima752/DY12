class InvalidInputError(Exception):
    pass

def sequential_subtract(numbers):
    if len(numbers) < 2:
        raise InvalidInputError("The list must contain at least two numeric elements.")
    
    result = numbers[0]
    
    for num in numbers[1:]:
        if not isinstance(num, (int, float)):
            raise InvalidInputError(f"Non-numeric value encountered: {num}")
        result -= num
    
    return result
try:
    result = sequential_subtract([10, 3, 2, 1])
    print("Result:", result)
except InvalidInputError as e:
    print(e)

try:
    result = sequential_subtract([10])
    print("Result:", result)
except InvalidInputError as e:
    print(e)

try:
    result = sequential_subtract([10, "abc", 2])
    print("Result:", result)
except InvalidInputError as e:
    print(e)
