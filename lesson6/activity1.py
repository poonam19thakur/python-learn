day = input('Enter the day:') .upper()
weather = input('Enter current weather:').lower()
homework = input('homework done (yes|no):')

print(f'Your plan for the {day}:')

if day in ('sunday','saturday'):
    print('Weekend.')
elif day == 'monday':
    print('First day of week.')
elif day == 'friday':
    print('Last day of school.')

elif day in ('tuesday','wednesday','thursday'):
    print('Regular days.')
else:
    print('Day not recognised.')


if weather == 'sunny' and homework =='yes':
    print('Go to the park.')
elif weather == 'rainy' and not (homework == 'yes'):
    print('Stay in ,do your homework.')
elif weather == 'sunny' and homework =='yes' and not day in ('saturday','sunday'):
    print('Great day all set up for school.')
else:
    print('One step at a time.')


print('have a wonderful day')