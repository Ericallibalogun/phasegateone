#display the  two numbers to the user
#prompt the user to input the answer,store as answer
#if the answer inputed by the user is not the equal to the result of the addition ; display false 
#if the answer inputed by the user is  equal to the result of the addition ; display true 




print('''

What is the sum of 20 and 40
				 ''')

answer = int(input('Enter your answer below:'))

if answer == 60:
	print('True')

if answer != 60:
	print('False')