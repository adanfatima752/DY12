import math

def round_float_to_int(f, strategy):
    if strategy == "up":
        return math.ceil(f)
    elif strategy == "down":
        return math.floor(f)
    elif strategy == "nearest":
        return round(f)
    else:
        raise ValueError("Invalid rounding strategy. Choose 'up', 'down', or 'nearest'.")
