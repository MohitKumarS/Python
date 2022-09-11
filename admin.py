def add_employee(emp_id, emp_name, emp_DOJ, emp_designation, emp_salary):
    file1 = open('employee.txt', 'a')
    file2 = open('login.txt', 'a')
    emp = emp_id + ',' + emp_name + ',' + emp_DOJ + ',' + emp_designation + ',' + emp_salary + '\n'
    l = emp_name.split()
    emp_login = emp_id + ' ' + l[0]+'\n'
    file1.writelines(emp)
    file2.writelines(emp_login)
    file1.close()
    file2.close()
    return "Employee added Successfully"

def see_employee_file(): 
    print()
    print("Details of employee = ")
    file = open('employee.txt','r')
    r = file.read()
    print(r)
    file.close()

def search_employee():   
    print()
    s_e = input("Enter the Employee ID = ")
    file = open('employee.txt','r')
    s = file.readlines()
    print("Status = ",end = "")
    counter = 0
    for i in s:
        for j in i.split():
            if s_e == j:
                print("Employee found")
                print("Details of the searched employee is = ",i)
                counter += 1
                break
    if counter == 0:
        print("Employee not found . ")
    file.close()
    
    
def remove(emp_id, files, s):
    f = open(files, 'r')
    a = f.readlines()
    for i in range(len(a)):
        j = a[i].split(s)
        if j[0] == emp_id:
            a[i] = ''
            break
    f.close()
    f = open(files, 'w')
    f.writelines(a)
    f.close()

def remove_employee(emp_id):
    remove(emp_id, 'employee.txt', ',')
    remove(emp_id, 'hr.txt', ',')
    remove(emp_id, 'login.txt', ' ')
    
    
def check(emp_id):
    flag = False
    file = open("employee.txt", 'r')
    employee = file.readlines()
    for i in employee:
        j = i.split(',')
        if j[0] == emp_id:
            flag = True
    return flag


def add_hr(emp_id, hr_dept, hr_role):
    file = open('hr.txt', 'a')
    hr = emp_id + ',' + hr_dept + ',' + hr_role + '\n'
    file.writelines(hr)
    file.close()
    return "HR added successfully"

    
def see_hr_file():   
    print()
    print("Details of HR's = ")
    file_ = open('hr.txt','r')
    r = file_.read()
    print(r)
    file_.close()

def search_HR(): 
    print()
    s_HR = input("Enter the ID = ")
    file_ = open('hr.txt','r')
    s = file_.readlines()
    counter = 0
    print("Status = ",end = "")
    for i in s:
        for j in i.split():
            if s_HR == j:
                print("Employee found")
                print("Details of the searched employee is = ",i)
                counter += 1
                break
     
    if counter == 0:
        print("Employee not found . ")
    file_.close()
    
    
def remove_hr(emp_id):
    remove(emp_id, 'hr.txt', ',')


while 1:
    print("Welcome to admin!!")
    print("Enter 1 to add employee\nEnter 2 to see employee file\nEnter 3 to search employee\nEnter 4 to remove employee\n"
          "Enter 5 to add hr\nEnter 6 to see hr file\nEnter 7 to search hr\nEnter 8 to remove hr\nEnter q to exit")
    n = input("Enter your Option: ")
    if n == '1':
        emp_id = input("Employee ID - ")
        emp_name = input("Employee Name - ")
        emp_DOJ = input("Date of Joining - ")
        emp_designation = input("Designation: ")
        emp_salary = input("Salary: ")
        print(add_employee(emp_id, emp_name, emp_DOJ, emp_designation, emp_salary))
    elif n == '2':
        see_employee_file()
        print()
    elif n == '3':
        search_employee()
        print()
    elif n == '4':
        emp_id = input("Employee ID - ")
        remove_employee(emp_id)
    elif  n == '5':
        emp_id = input("Employee ID - ")
        if (check(emp_id)):
            hr_dept = input("HR Department - ")
            hr_role = input("HR Role ")
            print(add_hr(emp_id, hr_dept, hr_role))
        else:
            print("Employee does not exist")
            break
    elif n == '6':
        see_hr_file()
        print()
    elif n == '7':
        search_HR()
        print()
    elif n == '8':
        emp_id = input("Employee ID - ")
        print("Is he/she leaving the company totally?")
        y = input("Enter yes or no: ")
        if y == 'yes':
            remove_employee(emp_id)
        else:
            remove_hr(emp_id)
    elif n == 'q':
        print("Thank You For Using This Program!")
        break