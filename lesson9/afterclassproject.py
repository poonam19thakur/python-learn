print("==✨=================😊=================✨==")
print("=========== HOLIDAY ACTIVITY PLANNER =========")
print("==✨=================😊=================✨==")
print("Choose holiday location:")
print("1 = Beach Holiday ⛱")
print("2 = Mountain Holiday🗻")
choose_holiday = int(input("Choose Holiday location(1|2):"))
if choose_holiday == 1:
    print("Choose 1 = Surfing🏄")
    print("Choose 2 = Sun Bathing 🔽 \n","☀\n\n\n","_________⛱_________")
    activity_beach = int(input("Choose Activity (1 🏄|2 ⛱) : "))
    if activity_beach == 1:
        print("REMEMEBER :\n","🎯 Don't forget to pack your SURF BOARD🛹\n","Enjoy your summer break🎉🎉")
    elif activity_beach ==2:
        print("REMEMEBER :\n","🎯 Don't forget to pack your UMBRELLA ⛱ AND SUMMER CLOTHES👚\n","Enjoy your summer break🎉🎉")
    else:
        print("💀Error💀\n","Please enter 1 or 2🙏")
elif choose_holiday == 2:
    print("Choose 1 = Skiing⛸")
    print("Choose 2 = Hiking⛑")
    activity_mountains = int(input("Choose Activity (1 ⛸|2 ⛑) : "))
    if activity_mountains == 1:
        print("REMEMEBER :\n","🎯 Don't forget to pack your SKI BOOTS⛸\n","Enjoy your summer break🎉🎉")        
    elif activity_mountains == 2:
        print("REMEMEBER :\n","🎯 Don't forget to pack your FIRST AID KIT⛑\n","Enjoy your summer break🎉🎉")
    else:
        print("💀Error💀\n","Please enter 1 or 2🙏")
else:
    print("💀Error💀\n","Please enter 1 or 2🙏")
print("===✨=================😊=================✨====")
print("=========== ENJOY YOUR SUMMER HOLIDAY ==========")
print("===✨=================😊=================✨====")