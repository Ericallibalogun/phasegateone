#list the number of days in an array
#prompt the user to input a number for todays day,store as today
#prompt the user to input a number for day elapsed,store as noOfDays
#calculate for future day by adding today and noOfToday mod 7(i.e no of days in a week ) 
#display the result to the user showing the present day and the future day







days_of_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

today = int(input('Enter today day(0 for Sunday,1 for Monday......6 for Saturday): '))


no_of_day = int(input('Enter the number of days elapsed since today: '))

future_days = (today + no_of_day) % 7

print(f'Today is {days_of_the_week[today]} and the future day is {days_of_the_week [future_days]}')