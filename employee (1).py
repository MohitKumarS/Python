def check_hr(id):
    flag = False
    file = open("hr.txt", 'r')
    hr = file.readlines()
    for i in hr:
        j = i.split(',')
        if id == j[0]:
            flag = True
    return flag


def view_details(id):
    file = open("employee.txt", 'r')
    emp = file.readlines()
    for i in emp:
        j = i.split(',')
        if id == j[0]:
            return i
    else:
        return "Employee doesn't exist"


def view_employee(designation):
    print()
    file = open('employee.txt', 'r')
    emp = file.readlines()
    for i in emp:
        j = i.split(',')
        if designation == j[3]:
            print(i)
    return 0


def view_hr():
    print()
    print("Details of HR's = ")
    file_ = open('hr.txt','r')
    r = file_.read()
    print(r)
    file_.close()
    


__name__ == '__main__'
username = input("Enter the id again: ")
print()
if check_hr(username):
    while 1:
        print('enter 1 to view details\nenter 2 to view all employees\nenter q to exit')
        print()
        n = input("Enter your choice: ")
        if n == '1':
            print(view_details(username))
        elif n == '2':
            designation = input("Enter designation: ")
            view_employee(designation)
        elif n == 'q':
            print()
            print("Thank You for Using this Program!")
            break
else:
    while 1:
        print('enter 1 to view details\nenter 2 to view all HR names\nenter q to exit')
        print()
        n = input("Enter your choice: ")
        if n == '1':
            print(view_details(username))
        elif n == '2':
            view_hr()
            print()
        elif n == 'q':
            print()
            print("Thank You for Using this Program!")
            break
