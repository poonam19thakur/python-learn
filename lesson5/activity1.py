temperature = int(input("Enter the temperature in Celsius: "))
if temperature < 20:
    print('It is cold today wear a jacket')
else:
    print('It is warm today you can wear a t-shirt')

is_raining = input('Is it raining today? (yes|no)')
if is_raining == 'yes':
    print('It is raining today wear raincoat.')

wind_speed = int(input('Enter wind speed:'))
if wind_speed > 30:
    print(' It is windy today Needed windbreaker.')
else:
    print('It is calm today no need of windbreaker.')

has_puddles = input('Does the road have puddles?(yes|no)')
if has_puddles == 'yes':
    print('Road has puddles wear boots.')
else:
    print('Road has no puddles wear sneakers.')

print('----------------------------------------')
print('Weather check complete')
print('Temperature:',temperature)
print('Is raining:',is_raining)
