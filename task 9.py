def split_and_join_with_condition(s, split_delimiter, join_delimiter, condition_func):
    
    parts = s.split(split_delimiter)
    
    filtered_parts = [part for part in parts if condition_func(part)]
    
    result = join_delimiter.join(filtered_parts)
    
    return result

def length_greater_than_3(s):
    return len(s) > 3
