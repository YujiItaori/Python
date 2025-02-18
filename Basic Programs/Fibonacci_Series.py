# Iterative Approach
def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

# Recursive Approach
def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Example Usage
fibonacci_iterative(10)  # Output: 0 1 1 2 3 5 8 13 21 34
print(fibonacci_recursive(10))  # Output: 55 (10th Fibonacci number)
