numbers = [0, 1]
num1 = numbers[0]
num2 = numbers[1]

for a in range(0, 98):
    #Add the first two numbers to bet the next value in the fibonacci sequence.
    num3 = float(num1) + float(num2)
    numbers.append(num3)
    
    num1 = num2
    num2 = num3

for s in numbers:
    print(int(s))
