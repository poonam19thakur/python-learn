a = int(input('Maths no. '))
b = int(input('S.S.T no.'))
c = int(input('English no.'))
sum = a + b + c
average = sum/3

if average in range(91,100):
    print('A+')
elif average in range(81,90):
    print('B+')
