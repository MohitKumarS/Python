import getpass
print("______LOGIN SCRIPT______")
file = open("login.txt","r")
file1 = file.readlines()
username = input("Please Enter your Login ID => ")
for f in file1:
    if username in f:
        password = getpass.getpass("Please Enter your Password => ")
        if password in f:
            print("Logged in Successfully!")
            if username == 'admin':
                import admin
                break
            else:
                import employee
                break
        else:
            print("Incorrect Password!")
else:
    print("Invalid Login ID!")
        
