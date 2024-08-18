import re
from collections import Counter

def clean_string(s):
   
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return cleaned

def is_palindrome(s):
    return s == s[::-1]

def character_frequencies(s):
    return dict(Counter(s))

def process_string(s):
    cleaned = clean_string(s)
    palindrome_check = is_palindrome(cleaned)
    frequencies = character_frequencies(cleaned)
    
    return {
        "is_palindrome": palindrome_check,
        "frequencies": frequencies
    }

input_string = "A man, a plan, a canal, Panama!"
result = process_string(input_string)
print(result)
