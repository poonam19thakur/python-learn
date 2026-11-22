print("======WELCOME TO RIDE BUILDER======")
print("Choose your vehicle. ")
print("1 = Scooty")
print("2 = Car")
choose = int(input("Choose your ride (1|2): "))
if choose == 1:
    print("Choose your vehicle type: Electric or Petrol")
    print("1 = Electric")
    print("2 = Petrol")
    fuel_type = int(input("Vehicle Type: "))
    if fuel_type == 1:
       print("No helmet or license needed.")
    elif fuel_type == 2:
       print("You have more mileage.")
    else:
       print("Error! Enter (1|2)")
elif choose ==2:
    print("Choose your vehicle type: Diesal or Petrol")
    print("1 = Diesal")
    print("2 = Petrol")
    car_fuel = int(input("Fuel Type:"))
    if car_fuel == 1:
        print("You will get less mileage.")
    elif car_fuel == 2:
        print("You will get more mileage than diesal.")
    else:
       print("Error! Enter (1|2)")
else:
    print("Error!!,Please enter valid number...")

