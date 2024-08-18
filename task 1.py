def safe_convert_to_int_with_default(s, default):
    try:
        return int(s)
    except ValueError:
        return default
