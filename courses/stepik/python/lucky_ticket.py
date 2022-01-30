num = int(input())
num1 = num // 1000
num2 = num % 1000
sum1 = (num1 // 100) + ((num1 % 100)//10) + ((num1 %100) % 10)
sum2 = (num2 // 100) + ((num2 % 100)//10) + ((num2 %100) % 10)
#print(sum1,sum2)
if sum1 == sum2:
    print('Счастливый')
else:
    print('Обычный')