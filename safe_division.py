try:
    a = float(input("A: "))
    b = float(input("B: "))
    print("Result:", a / b)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Numbers only, please!")
