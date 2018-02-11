class Student:
    def __init__(self,f_name,l_name):
        self.f_name=f_name
        self.l_name=l_name
    def generateEmail(self):
        self.email=self.f_name.lower()+"."+self.l_name.lower()+"@deerwalk.edu.np"
    def display(self):
        print("Email : {}".format(self.email))
f_name=input("First Name: ")
l_name=input("Last Name: ")
s=Student(f_name,l_name)
s.generateEmail()
s.display()