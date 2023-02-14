def factorial(num):
    factorial = 1
    if num < 0:
        print("Factorial does not exist for - ve  numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1, num + 1):
            factorial = factorial * i

    return  factorial
print(factorial(4))
print(factorial(5))
print(factorial(6))


