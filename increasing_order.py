number1 = int(input('Enter first number: '))

number2 = int(input('Enter second number: '))

number3 = int(input('Enter third number: '))


print(/nnumber1,number2,number3)
print('In ascending order is: ')

minimum=number1
if minimum > number2:
	minimum = number2
elif minimum > number3:
	minimum = number3

maximum = number1
if maximum < number2:
    maximum = number2
if maximum < number3:
    maximum = number3

second_min = number1 + number2 + number3 - minimum - maximum


print(minimum, second_min, maximum)