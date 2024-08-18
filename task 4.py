def convert_strings_to_integers_with_logging(strings):
    integers = []
    error_log = []

    for s in strings:
        try:
            integers.append(int(s))
        except ValueError as e:
            error_log.append(f"Error converting '{s}': {e}")

    return integers, error_log
#example
strings = ["10", "abc", "20", "3.5", "40"]

integers, error_log = convert_strings_to_integers_with_logging(strings)

print("Integers:", integers)
print("Error Log:", error_log)
