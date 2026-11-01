# Student App Access Manager
 
#1.
camera = 1      
microphone = 2  
storage = 4     
location = 8   
 
# 2.
approved_apps = ("coding app","math app","reading app","science app")
 
# 3.
student_name = input("Enter your name: ")
requested_app = input("Enter the app you want to use: ").lower()
 
print("<=== Identity Operator Check ===>")
 
# 4.
if type(student_name) is str:
    print("The student name is stored as text.")
 
#5.
if type(requested_app) is not int:
    print("The requested app is not stored as a number.")
 
 
print("--- Membership Operator Check ---")
 
# 6.
if requested_app in approved_apps:
    print(requested_app, "is an approved student app.")
else:
    print(requested_app, "is not an approved student app.")
 
#7.
restricted_apps = ( "gaming app","shopping app","social media app")
 
if requested_app not in restricted_apps:
    print("The app is not in the restricted list.")
else:
    print("Access denied because the app is restricted.")
 
 
print("\n--- App Permission Settings ---")
 
# 8.
student_permissions = camera,microphone,storage


print("Permission of student:",student_permissions) 
#10.
if student_permissions & camera:
    print("Camera permission: Enabled")
 
elif student_permissions & microphone:
    print("Microphone permission: Enabled")
 
elif student_permissions & storage:
    print("Storage permission: Enabled")
 
elif student_permissions & location:
    print("Location permission: Enabled")
else:
    print("Location permission: Disabled")
 
 
print("--- Bit Shift Demonstration ---")
 
# Shift the CAMERA bit left to create the next permission value
next_permission = camera << 1
 
print("Camera bit:", bin(camera))
print("After left shift:", bin(next_permission))
 
# Shift the STORAGE bit right
previous_permission = storage >> 1
 
print("Storage: ",storage)
print("After right shift:", bin(previous_permission))
 
 
print("\n--- Final Access Result ---")
 
# Check both app approval and permission availability
if requested_app in approved_apps and requested_app not in restricted_apps:
    print("Access granted to", requested_app)
else:
    print("Access denied to", requested_app)





