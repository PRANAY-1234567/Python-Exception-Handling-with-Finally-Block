print("Program starts...")
a = 0
b = 0
c = 0

try:
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))

    c = a // b  # Integer division like Java

except ValueError:
    print("Error in data : Number not provided correctly")

except ZeroDivisionError:
    print("Error in data : Divisor should not be zero")

except Exception as e:
    print("Error in data :", e)

finally:
    print("The division of", a, "and", b, "is", c)

print("Program ends...")
