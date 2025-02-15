# python program for Leap Year Detector

leap = int(input("Enter Year: "))

if leap % 4 == 0 or leap % 400 == 0:
    print(f"{leap} is a leap year")
elif leap % 100 == 0:
    print(f"{leap} not a leap year")
else:
    print(f"{leap} not a leap year")
