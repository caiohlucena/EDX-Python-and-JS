import sys

try:
    x = int(input("x: "))
    y= int(input("y: "))
except ValueError:
    print ("Invalid input")
    sys.exit(1)

    
try:
    dev = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
    sys.exit(1)
print (f"{x}/ {y} = {dev}")


