num1 = int(input())
num2 = int(input())
num3 = int(input())
num_count = 0
if num1 == num2:
    num_count += 1
if num2 == num3:
    num_count += 1
if num1 == num3:
    num_count += 1
if num_count == 1:
    num_count = 2
print(num_count)
