#           BONUS WORK

# Setting numbers to an empty list.
numbers = []

# Defining a function called validateAdd
def validateAdd(v):
    if v.isdigit():
        numbers.append(v)
    else:
        print(v + ' is not a number')


while len(numbers) < 2:
    numberInput1 = input('Enter a number ')
    validateAdd(numberInput1)
    
num1 = numbers[0]
num2 = numbers[1]


for a in range(0, 10):
    num3 = float(num1) + float(num2)
    numbers.append(num3)
    
    num1 = num2
    num2 = num3

for s in numbers:
    print(int(s))
