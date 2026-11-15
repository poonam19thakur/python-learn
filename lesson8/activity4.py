a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
average = (a+b+c)/3

print("Average = ",average)

if average > a and average > b and average > c:
    print("%d is higher than %d, %d, %d" %(average,a,b,c))