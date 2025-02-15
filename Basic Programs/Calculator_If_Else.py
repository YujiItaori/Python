# calculator using if else

def cal(a , b , c):
    if a == "+":
        return b + c
    elif a == "-":
        return b - c
    elif a == "/":
        return b / c
    elif a == "*":
        return b * c

first_value = int(input("Enter First Value: "))
second_value = int(input("Enter Second Value: "))
action = input("Enter action from + - / * : ")
result = cal(action, first_value, second_value)
print(result)
