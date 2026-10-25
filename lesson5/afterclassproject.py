#1.
homework_time = int(input('Enter your homework time(In Mins)'))

#2.
if homework_time > 60:
    print('That is a long homework session.')
else:
    print('That is a short homework session.')

#3.
free_time = input('Is there free time after homework? (yes/no)')
if free_time == 'yes':
    print('You should play with sister.')

#4.
print("<========== DAILY PLAN ==========>")
print('Homework Time:',homework_time)
print('Free Time:',free_time)
print("<=========== CARRY ON ============>")
