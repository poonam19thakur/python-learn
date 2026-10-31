import keyword 
print('\nPython keywords are:\n',keyword.kwlist)

Name = input('Enter your name: ')
School = input('Enter School Name: ')
Admission_number = int(input('Enter your Admission Number: '))
Address = input('Enter your Address: ')
Father_name = input('Enter your father name: ')
Mother_name = input('Enter your mother name: ')
father_number = int(input('Enter your father number: '))
Mother_number = int(input('Enter your mother number: '))
Admission_number_text =  str(Admission_number)
father_number_text =  str(father_number)
Mother_number_text =  str(Mother_number)

first_three = Name[0:3]
last_letter = Name[::-1]
code_name = (first_three + last_letter)



print('Code name is: ',code_name)
print('Name: \n',Name,'Type: \n',type(Name))
print('School: \n',School,'Type: \n',type(School))
print('Admission number: \n',Admission_number,'Type: \n',type(Admission_number))
print('Address: \n',Address,'Type: \n',type(Address))
print('Father Name: \n',Father_name,'Type: \n',type(Father_name))
print('Mother_name: \n',Mother_name,'Type: \n',type(Mother_name))
Attendance = 360


print('Attendance: ',Attendance)
Attendance += 20


print('Attendance after 20 days attend of school: ',Attendance)
Attendance -= 7


print('Attendance after 1 week absent from school: ',Attendance)

average = Attendance/10

print('Average attendance: ',average)

points = 3600
box_storage = 20
box_needed = 3600//20
points_left = 3600%20
print('Points: \n',points,'Box storage: \n',box_storage,'Box Needeed: \n',box_needed,'Points left: \n',points_left)

last_year_points = 387
if points >= last_year_points:
    print('Better than last year.')
else:
    print('False')
if points == last_year_points:
    print('Equal to last year.')
else:
    print('False')
if points <= last_year_points:
    print('Less than last year.')
else:
    print('False')


print('<===============STUDENT IDENTITY CARD================>')
print('Student name: ',Name)
print('Code name is: ',code_name)
print('School: ',School)
print('Admmission Number: ',Admission_number)
print('Father name: ',Father_name)
print('Mother name: ',Mother_name)
print('Address: ',Address)
print('Attendance: ',Attendance)
print('Average Attendance: ',average)
print('<=====================================================>')