number1 = int(input())
number2 = int(input())
number3 = int(input())
if number1 >= number2:
    if number1 >= number3:
        print(number1)
elif number2 >= number3:
    print(number2)
else:
    print(number3)
