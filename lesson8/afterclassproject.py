#1.
print("=========== GROCERY COST COMPARISON TOOL ===========")

#2.
rice_price = 12  
chocolate_price = 4          
milk_price = 4             
number_of_baskets = 2     
family_members = 4  
total_price = rice_price + chocolate_price + milk_price
item_in_basket = total_price * number_of_baskets
cost_per_person = item_in_basket / family_members

print("Total price of items in the basket:", item_in_basket)
print("Cost per person:", cost_per_person)

#3.
total_items = int(input("Enter the total number of items: "))
people = int(input("Enter the number of people: "))
left_items = total_items // people

if total_items % people == 0:
    print("Items are equally distributed.")
else:
    print("Each person gets", left_items, "items.")

#4.
weekly_average = 95.6     
store_a_average = 50     
store_b_average = 40       
store_c_average = 80 

if cost_per_person < store_a_average and cost_per_person < store_b_average and cost_per_person < store_c_average:
   verdict = "cheaper than all three stores"
elif cost_per_person > store_a_average and cost_per_person > store_b_average and cost_per_person > store_c_average:
   verdict = "more expensive than all three stores"
else:
   verdict = "Somewhere in between the three stores"

#5.
print("\n=========== SUMMARY ===========")                                   
print("Cost per person this week:", cost_per_person)         
print("Weekly average           :", weekly_average)         
print("Verdict                  :", verdict)
print("===========!Happy Ending!===========")
