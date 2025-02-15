# Given number is Positive, Negative, or Zero

value = int(input("Enter number: "))

if value > 0:
    print(f"{value} is a Positive number")
elif value < 0:
    print(f"{value} is a Negative number")
else:
    print(f"{value} is Neutral")
