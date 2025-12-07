

def is_palindrome(s: any) -> bool:
    # Remove non-alphanumeric characters and convert to lowercase
    convert = str(s)
    cleaned = ''.join(char.lower() for char in convert if char.isalnum())
    # Check if the cleaned string is equal to its reverse
    return cleaned == cleaned[::-1]

# Example usage:
print(is_palindrome("A man, a plan, a canal, Panama"))  # Output: True
print(is_palindrome("race a car"))  # Output: False 
print(is_palindrome(12321))  # Output: True
print(is_palindrome(12345))  # Output: False