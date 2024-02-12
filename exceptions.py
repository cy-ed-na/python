# Excceptions - errors

try:
    print(x)
except:
    print("An error occured")
finally:
    print("success")
num = 20
num2 = 0


try:
    print(num / num2)
except:
    print("Zero division error occured")

# user defined functions
try:
 def multiply(number1, number2):
    print(number1 * number2)
except:
    print("An error occured")
finally:
    print("Success")

