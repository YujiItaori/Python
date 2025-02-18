import math

def find_lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def find_gcd(a, b):
    return math.gcd(a, b)

# Example Usage
a, b = 12, 18
print("GCD:", find_gcd(a, b))  # Output: 6
print("LCM:", find_lcm(a, b))  # Output: 36
