import datetime

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

    def increase_salary(self, percent):
        if percent > 0:
            self.set_salary(self.salary + self.salary * percent)
        else:
            print("Increase of salary must be greater than 0.")

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


emp1 = Employee('Jack', 'Krichen', 'Manager', 50000, 1)

print(emp1.get_firstname())
print(emp1.get_lastname())
print(emp1.get_employeeid())
print(emp1.get_jobtitle())
print(emp1.get_salary())

print(emp1.get_vacation_days())
emp1.take_vacation_days(10)
print(emp1.get_vacation_days())
emp1.take_vacation_days(10)
emp1.take_vacation_days(-1)

emp1.increase_vacation_days_yearly()
print(emp1.get_vacation_days())


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
    
con = Contractor('Temp','Emp','Developer',60,2)
print(con.get_firstname())
print(con.get_lastname())
print(con.get_contractorid())
print(con.get_jobtitle())
print(con.get_hourlywage())
print(con.set_hourlywage(50))
print(con.get_hourlywage())