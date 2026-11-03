#1.
student_name = input('Enter student name: ')
requested_app = input('Enter the type of app you need: ')

#2.
approved_apps = ('Coding app' , 'Study app')

if requested_app in approved_apps:
    print('App is approved for student.')
else:
    print('App is not approved for student.')
 
#3.
microphone_working = input('Is your microphone working (yes|no): ')
camera_working = input('Is your camera working (yes|no): ')
storage = int(input('Storage in your device: '))

#4.
restricted_apps = ('Gaming App','Shopping App','Social media app')

#5.
if microphone_working is 'yes' and requested_app in restricted_apps:
    print('You can use the app.')
elif camera_working is not 'yes' or requested_app in restricted_apps:
    print('You can not use the app.')
elif storage > 100 and requested_app in restricted_apps:
    print('You can use the app.')
else:
    print('You cannot use the app.')

#6.Final result
print("<==========> Final Result <==========>")
if requested_app in approved_apps and requested_app not in restricted_apps:
    print("Access granted to", requested_app)
else:
    print("Access denied to", requested_app)
print('<=============> Keep up <=============>')