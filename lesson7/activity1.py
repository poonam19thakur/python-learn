x = 7
print(type(x) is int)

x = 7.9
print(type(x) is float)

x = 34
y = 34

if x is y:
    print('x and y are same.')
else:
    print('x and y are not same.')


y = 13

if x is not y:
    print('X and Y have different identity.')