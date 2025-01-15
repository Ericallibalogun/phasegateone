import array

item = [[1,2], [2,3,],[3,4],[4,5],[5,6]]
print('a\t\tb\t\ta**b')

for row in item:

	a, b = row
	result = a ** b
	print(f'{a}\t\t{b}\t\t{result}')