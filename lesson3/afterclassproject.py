name = input('Enter member name:')
club = input('Enter club name:') 

member_number = 8
points = 8.5
is_active = True
print('Name:',name,'type:',type(name))
print('club',club,'type',type(club))
print('member number:',member_number,'type:',type(member_number))
print('points',points,'type',type(points))
print('is active',is_active,'type',type(is_active))

first_three = name[0:3]
last_letter = name[-1]
member_number_text = str(member_number)
points_text = str(points)
is_active_text = str(is_active)
print('member number as text:',member_number_text,'type:',type(member_number_text))
print('Points as text:',points_text,'type:',type(points_text))
print('Is active:',is_active_text,'type:',type(is_active_text))

badge_code = member_number_text  + first_three + last_letter
print(badge_code)
badge_line_1 = 'Member:' + name.upper()
badge_line_2 = 'Club:'+ club.upper()
badge_line_3 = 'Code:' + badge_code.upper()
badge_line_4 = 'Points:' + points_text
badge_line_5 = 'Active:' + is_active_text


print("===== CLUB BADGE =====")
print(badge_line_1)
print(badge_line_2)
print(badge_line_3)
print(badge_line_4)
print(badge_line_5)
print("========= VIP =========")