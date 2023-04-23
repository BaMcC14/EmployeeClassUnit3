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

#Get employee id 
def get_employeeid(self):
    return "Employee ID: " + str(self.employeeid)

#Return Salary
def get_salary(self):
    return "${:,.2f}".format + (self.salary)

#Set Salary
def set_salary(self, sal):
    if sal > 0:
        self.salary = sal

def increase_salary(self, percent):
    if percent > 0:
        self.set_salary(self.salary + self.salary * percent)
    else:
        print("Increase of salary must be greater than 0.")

