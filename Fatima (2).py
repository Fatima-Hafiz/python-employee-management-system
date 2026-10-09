from datetime import datetime

def main_menu():
    print(" ***  EMS  ***")
    print(" 1. Employee Records Management")
    print(" 2. Role and Department Management")
    print(" 3. Salary Management")
    print(" 4. Quit")


def add_emp_detail():
    empid=input('Enter employee id =')
    if not empid.isdigit():
        print("Invalid employee id, please enter numbers only")
        return
    try:
        with open("employee_record.txt","r") as g:
            data=g.readlines()
            for record in data:
                fields=record.strip().split("*")
                if fields[0]==empid:
                    print("Employee id is already exisit")
                    return
    except:
        pass
    print("Choose gender:")
    print("1.Female")
    print("2. Male")
    choice=input("Enter choice(1 or 2):")
    if choice=="1":
        gender="Female"
    elif choice=="2":
        gender="Male"
    else:
        print("Invalid gender choice")
        return
    name=input('Enter employee name =')    
    phonenumber=input('Enter phone_number =')
    jdate=input('Enter join date (DD-MM-YYYY)=')  
    f=open('employee_record.txt','a+')
    myString=str(empid)+'*'+name+'*'+gender+'*'+str(phonenumber)+'*'+jdate+'\n'
    f.write(myString)
    f.close()
    print("employee added successfully")


def view_emp_list():
    try:
        g=open('employee_record.txt','r')
        data=g.readlines()
        if not data:
            print("no employee records found")
            g.close()
            return
        for record in data:
            print(record.strip())
        g.close()
    except:
        print("no employee records found")


def update_emp_information():
    empid=input("Enter the emp id for updation =")
    found= False
    try:
        with open("employee_record.txt","r")as g:
            data=g.readlines()
    except:
        print("No employee record found")
        return
    
    with open("employee_record.txt","w+")as g:
        for record in data:
            fields=record.strip().split("*")
            if(empid==fields[0]):
                name=input("Enter the update name =")
                print("select updated gender:")
                print("1.Female")
                print("2.Male")
                choice=input("Enter choice(1 or 2):")
                if choice=="1":
                    gender="Female"
                elif choice=="2":
                    gender="Male"
                else:
                    print("Invalid gender choice")
                    return          
                phonenumber=input("Enter the update phonenumber =")
                jdate=input("Enter the update jdate =")
                record=fields[0]+"*"+name+"*"+gender+"*"+str(phonenumber)+"*"+jdate+"\n"
                found= True
            g.write(record)
            
    if found:
        print("record updated")
    else:
        print("employee id not found")


def delete_emp_record():
    empid=input("Enter employee id to delete: ")
    g=open("employee_record.txt","r")
    data=g.readlines()
    g.close()
    found=False
    g=open("employee_record.txt","w")
    for record in data:
        fields=record.strip().split("*")
        if empid!=fields[0]:
            g.write(record)
        else:
            found=True
    g.close()
    if found:
        print("Employee deleted")
    else:
        print("Employee id not found")


def checkid1(empid):
    try:
        with open("employee_record.txt","r") as g:
            data=g.readlines()
        for record in data:
            fields=record.strip().split("*")
            if fields[0]==empid:
                return True,fields[1],fields[2],fields[4].strip()
    except:
        pass
    return False,"","",""
def assign_dept_role():
    empid=input("Enter employee id: ")
    flag,name,gender, _ =checkid1(empid)
    
    if not flag:
        print("Employee not found")
        return
    print("Choose department: ")
    print("1. CFS (Center for Foundation Studies)")
    print("2. DCS (Department of Computing Sciences)")
    print("3. DBMS (Department of Business Management Studies)")
    print("4. Management ")
    try:
        dept_choice=int(input("choose from (1-4): "))
    except:
        print("invalid entry, please choose from(1-4)")
        return
    if dept_choice==1:
        department="CFS"
    elif dept_choice==2:
        department="DCS"
    elif dept_choice==3:
        department="DBMS"
    elif dept_choice==4:
        department="Management"
    else:
        print("invalid entry, please choose from (1-4)")
        return

    print("choose role: ")
    print("1. Lecturer ")
    print("2. Manager ")
    print("3. Admin ")
    role_choice=int(input("choose from (1-3): "))
    if role_choice==1:
        role="Lecturer"
    elif role_choice==2:
        role="Manager"
    elif role_choice==3:
        role="Admin"
    else:
        print("invalid entry, please choose from(1-3)")
        return

    try:
        with open("employee_dept_role.txt","r") as g:
            data=g.readlines()
    except:
        data=[]

    updated=False
    g=open("employee_dept_role.txt","w")
    for record in data:
        fields=record.strip().split("*")
        if fields[0]== empid:
            g.write(empid+"*"+name+"*"+department+"*"+role+"\n")
            updated= True
        else:
            g.write(record)
    if not updated:
        g.write(empid+"*"+name+"*"+department+"*"+role+"\n")
    g.close()
    print("Department and role assigned")


def view_dept_role():
    try:
        g=open("employee_dept_role.txt","r")
        data=g.readlines()
        if not data:
            print("no department/role data found")
            g.close()
            return
        for record in data:
            print(record.strip())
        g.close()
    except:
        print("no department/role data found")


def set_salary_details():
    empid=input('Enter employee id =')
    exists, name, gender, jdate= checkid1(empid)
    if not exists:
        print("This employee id does not exist")
        return
    try:
        with open("employee_record.txt","r") as g:
            data=g.readlines()
    except:
        print("No employee record found")
        return
    found=False
    for record in data:
        fields=record.strip().split("*")
        if fields[0]==empid:
            found=True
            name=fields[1]
            gender=fields[2]
            jdate=fields[4]
            break
    if not found:
        print("Employee id not found")
        return
    try:
        jdate = datetime.strptime(jdate, "%d-%m-%Y")
        today=datetime.today()
        numyrs=today.year - jdate.year - ((today.month, today.day)< (jdate.month, jdate.day))
    except:
       print("invalid jdate")
       return
    print("Years of service= ",numyrs)

    role = ""
    try:
        with open("employee_dept_role.txt","r") as g:
            data=g.readlines()
        for record in data:
            fields=record.strip().split("*")
            if fields[0]==empid:
                role=fields[3]
                break
    except:
        pass
        
    if role=="Admin":
        base=800
    elif role=="Lecturer":
        base=1000
    elif role=="Manager":
        base=1200
    else:
        base=900
        

    bonus=base*(1.5/100)*numyrs
    deduction=(base*0.05)*int(numyrs/5)
    total=base + bonus - deduction
    record=empid+"*"+name+"*"+str(base)+"*"+str(bonus)+"*"+str(deduction)+"*"+str(total)+"\n"
    g=open("employe_set_salary.txt","a+")
    g.write(record)
    g.close()
    print("salary of employee" ,empid, "has been set ")
    print(record)


def calculate_view_monthly_salary():
    try:
        g=open("employe_set_salary.txt","r")
        data=g.readlines()
        if not data:
            print("No salary record found")
            g.close()
            return
        print("empid*name*base*bonus*deduction*total")
        for record in data:
            print(record.strip())
        g.close()
    except:
        print("No salary record found")


if __name__=="__main__":
 
    while(True):
        main_menu()
        ch=int(input("Enter 1 to 4 ==> "))
        if(ch==1):
            print(" a. add employee")
            print(" b. view employee list")
            print(" c. update employee information")
            print(" d. delete an employee record")
            choice=input("enter your choice ")
            if(choice=="a"):
                add_emp_detail()
            elif(choice=="b"):
                view_emp_list()
            elif(choice=="c"):
                update_emp_information()
            elif(choice=="d"):
                delete_emp_record()
            else:
                print("select proper input")
 
        elif(ch==2):
            print("a. assign dept & role")
            print("b. view dept/role")
            choice=input("enter your choice ")
            if(choice=="a"):
                assign_dept_role()
            elif(choice=="b"):
                view_dept_role()
            else:
                print("select proper input")
                
        elif(ch==3):
            print("a. set salary details")
            print("b. calculate & view monthly salary")
            choice=input("enter your choice ")
            if(choice=="a"):
                set_salary_details()
            elif(choice=="b"):
                calculate_view_monthly_salary()
            else:
                print("select proper input")
 
        elif(ch==4):
            print("good bye")
            continue
        else:
            print(" Invalid input")
