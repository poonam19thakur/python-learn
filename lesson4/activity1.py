# 1) Add the activity details.
# a) Mention the activity name as "Farm Harvest Calculator".
# b) Introduce the program as a harvest and earnings calculator.
feild1 = 20 
feild2 = 30
feild3 = 10
total = feild1 + feild2 + feild3
average = total/3

print('Total is:',total)
print('Average is:',average)

# 2) Store harvest values.
# a) Use the assignment operator `=` to store harvest from three fields.
# b) Store each field's harvest in separate variables.

# 3) Use arithmetic operators.

# a) Use `+` to calculate the total harvest.

# b) Use `/` to calculate the average harvest per field.

# c) Use `*` to calculate total earnings.

# 4) Display total, average, and earnings.
# a) Print the total harvest in kilograms.
# b) Print the average harvest per field.
price_per_kg = 50
earnings = price_per_kg*total

print('Total harvest is:',earnings)
# c) Print the total earnings in rupees.

# 5) Use floor division and modulus.

# a) Use `//` to calculate the number of full 25 kg bags.

# b) Use `%` to calculate the leftover grain.

bags_needed = total//25
leftover_grain = total%25

print('Bags needed:',bags_needed)
print('Leftover grain:',leftover_grain)
# c) Print the full bags and leftover amount.

# 6) Use comparison operators.

# a) Compare this year's harvest with last year's harvest.

# b) Use `>` to check if this year is better.

# c) Use `==` to check if both years are the same.

# d) Use `>=` to check if this year is at least as good.
last_year_grain = 200
print('Better than last year:',last_year_grain >= total)
print(total + 20)
# 7) Use assignment operators.

# a) Use `+=` to add bonus crop to the total.

# b) Use `-=` to subtract grain saved as seeds.

# c) Print the updated harvest after each change.

# 8) Calculate the final bag count.

# a) Use floor division again after adjustments.

# b) Print the final number of bags packed.

# """