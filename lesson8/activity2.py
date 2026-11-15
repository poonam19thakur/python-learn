numer = int(input('Enter a numerator:'))
denom = int(input('Enter a denominator:'))

if numer % denom == 0:
    print(numer,"is divisible by",denom)
else:
    print(numer,"is not divisible by",denom)