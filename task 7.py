def exponentiation_table(base, exponent_range):
    if not isinstance(base, (int, float)):
        raise ValueError("Base must be a numeric value.")
    if not isinstance(exponent_range, int) or exponent_range < 1:
        raise ValueError("Exponent range must be a positive integer.")

    table = []
    for i in range(1, exponent_range + 1):
        result = base ** i
        table.append(f"{base}^{i} = {result}")
    
    return table
try:
    table = exponentiation_table(2, 5)
    for line in table:
        print(line)
except ValueError as e:
    print(e)

try:
    table = exponentiation_table(3, 3)
    for line in table:
        print(line)
except ValueError as e:
    print(e)

try:
    table = exponentiation_table(2, "abc")
    for line in table:
        print(line)
except ValueError as e:
    print(e)
