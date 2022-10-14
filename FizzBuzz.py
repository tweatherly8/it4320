#print numbers 1-100
for num in range(1,101):
    #print FizzBuzz for multiples of 3 & 5
    if num % 15 is 0:
        print("FizzBuzz")
    #print Buzz for multiples of 5
    elif num % 5 is 0:
        print("Buzz")
    #print Fizz for multiples of 3
    elif num % 3 is 0:
        print("Fizz")
    else:
        print(num)
