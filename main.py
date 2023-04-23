import datetime

class Employee:
    def __init__(self, fname, lname, empid, title, sal):
        self.firstname = fname
        self.lastname = lname
        self.employeeid = empid
        self.jobtitle = title
        self.salary = sal

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

