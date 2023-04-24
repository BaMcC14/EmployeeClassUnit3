import datetime
import csv
import sys

#File used to store employee information (Employee ID and Salary)
FILENAME = 'employees.csv'

#exiting the program 
def exit_program():
    print("Terminating program.")
    sys.exit()

#Read the employees from the employees.csv file
def read_employees():
    try:
        employees = []
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                employees.append(row)
            return employees
    except FileNotFoundError as error:
        print(f"Could not find {FILENAME} file.")
        exit_program()
    except Exception as e:
        print(type(e), e)
        exit_program

#Writing to employees file
def write_employees(employees):
    try:
        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(employees)
    except Exception as e:
        print(type(e), e)
        exit_program()

#add employee to the list
def add_employee(employees):
    empid = input("Enter the employee ID: ")
    sal = input("Enter the salary of the employee: ")
    employee = [empid,sal]
    employees.append(employee)
    write_employees(employees)
    print(f"Employee {empid}: {sal} was added.\n")

#display the list of employees
def list_employees(employees):
    for i, employee in enumerate(employees, start = 1):
        print(f"{i} Employee ID: {employee[0]} (${employee[1]})")
    print()

#delete an employee based on ID
def delete_employee(employees):
    found = False
    number = input("Enter in the employee ID: ")
    for i, employee in enumerate(employees, start=0):
        if(employee[0] == number):
            print(f"Employee was deleted.\n")
            employee = employees.pop(i)
            found = True
        
    if(found == False):
        print("Employee not found")
    else:
        write_employees(employees)

#menu to display options.
def display_menu():
    print("The Employee Salary List Program")
    print()
    print("LIST OF COMMANDS")
    print("list - List all employees")
    print("add - Add an employee")
    print("del - Delete an employee")
    print("exit - Exit program")
    print()

display_menu()
employees = read_employees()
while True:
    command = input("Command: ")
    if command.lower() == 'list':
        list_employees(employees)
    elif command.lower() == 'add':
        add_employee(employees)
    elif command.lower() == 'del':
        delete_employee(employees)
    elif command.lower() == 'exit':
        break
    else:
        print("Not a valid command. Please try again.\n")
print("Ending Salary Program")


class Person:
    def __init__(self, fname, lname, title):
        self.firstname = fname
        self.lastname = lname
        self.jobtitle = title

        self.hiredate = datetime.date.today()

#returns first name
    def get_firstname(self):
        return self.firstname
    
#sets firstname if the fname isn't empty string
    def set_firstname(self, fname):
        if len(fname) > 0:
            self.firstname = fname

#returns last name
    def get_lastname(self):
        return self.lastname
#sets lastname if lname isn't an empty string    
    def set_lastname(self, lname):
        if len(lname) > 0:
            self.lastname = lname

#returns job title
    def get_jobtitle(self):
        return self.jobtitle
    
#sets job title if job title isn't an empty string
    def set_jobtitle(self, title):
        if len(title) > 0:
            self.jobtitle = title


class Employee(Person):
    def __init__(self, fname, lname, title, sal, empid):
        super().__init__(fname, lname, title)
        self.employeeid = empid
        self.salary = sal
        self.vacationdaysperyear = 14
        self.vacationdays = self.vacationdaysperyear

#Get employee id 
    def get_employeeid(self):
        return "Employee ID: " + str(self.employeeid)

#Return Salary
    def get_salary(self):
        return "${:,.2f}".format(self.salary)

#Set Salary
    def set_salary(self, sal):
        if sal > 0:
            self.salary = sal

#increase salary by a percent
    def increase_salary(self, percent):
        if percent > 0:
            self.set_salary(self.salary + self.salary * percent)
        else:
            print("Increase of salary must be greater than 0.")

#get vacation days
    def get_vacation_days(self):
        return "Vacation Days: " + str(self.vacationdays)

#increase vacation days per year. 
    def increase_vacation_days_per_year(self, days):
        if days > 0:
            self.vacationdaysperyear = self.vacationdaysperyear + days

#increase vacation days
    def increase_vacation_days(self, days):
        if days > 0:
            self.vacationdays = self.vacationdays + days

#increase vacation days by year
    def increase_vacation_days_yearly(self):
        self.vacationdays = self.vacationdays + self.vacationdaysperyear

#take some vacation days
    def take_vacation_days(self, days):
        if days > 0 and self.vacationdays - days >= 0:
            self.vacationdays = self.vacationdays - days
        elif days <= 0:
            print("Vacation days taken must be greater than 0.")
        elif self.vacationdays - days < 0:
            print(f"Employee does not have enought vacation days to take off {days} days.")


class Contractor(Person):
    def __init__(self, fname, lname, title, wage, contractorid):
        super().__init__(fname, lname, title)
        self.contractorid = contractorid
        self.hourlywage = wage

#return contractor id
    def get_contractorid(self):
        return 'Contractor ID: ' + str(self.contractorid)
    
#set hourly wage 
    def set_hourlywage(self, wage):
        if wage > 0:
            self.hourlywage = wage 

#return wage 
    def get_hourlywage(self):
        return "${:,.2f}".format(self.hourlywage)
    
#sets job wage if wage greater than 0
    def set_get_hourlywage(self, get_hourlywage):
        if get_hourlywage > 0:
            self.wage = get_hourlywage
    

