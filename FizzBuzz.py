for num in range(1,101):
    if num % 15 is 0:
        print("FizzBuzz")
    elif num % 5 is 0:
        print("Buzz")
    elif num % 3 is 0:
        print("Fizz")
    else:
        print(num)