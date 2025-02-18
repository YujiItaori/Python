def is_palindrome(s):
    return s == s[::-1]

# Example Usage
string = "madam"
number = "121"
print(is_palindrome(string))  # Output: True
print(is_palindrome(number))  # Output: True
