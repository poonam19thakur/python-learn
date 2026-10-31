#1.Giving Variables.
print('<==========Pool Requirement checker=========>')
age = int(input('Your age: '))
adult_here = input(' There is any adult with you (yes|no): ').lower()
can_swim = input('Can you swim (yes|no): ').lower()

#2.
if can_swim != 'yes' or can_swim != 'no':
    print('INPUT ERROR')
swim_known = True
if adult_here != 'yes' or adult_here != 'no':
    print('INPUT ERROR')
adult_known = False


if age < 5 and adult_here == 'yes':
    print("Age group   : child - small pool only, always with an adult.")
elif age < 12 and not (adult_here == 'yes'):
    print("Age group   : Teenager - main pool with an adult.")
elif age < 16 and can_swim == 'yes' or adult_here == 'yes':
    print("Age group   : Young - main pool alone if you can swim.")
elif age < 20 and can_swim == 'yes' or adult_here == 'yes':
    print("Age group   : Adult - all pools open to you.")
else:
    print("🔦💡No Entry💡🔦")
print('<==========Have A Safe Swim=========>')


