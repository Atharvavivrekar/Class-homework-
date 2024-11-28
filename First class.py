class Student():
    #Properties
    name = ""
    age = 12

    #constructer 
    def __init__ (self):
        print("creating a new student ")

    #functions
    def show_details(self):
        print("the details of a student ")
        print(self.name)
        print(self.age)



john = Student()    # First object 
alex = Student()    # second object
steve = Student()   # third object

john.show_details()

class Cars():
    #Properties
    name = ""
    year = 24

    #constructer 
    def __init__ (self):
        print("creating a new car ")

    #functions
    def show_details(self):
        print("the details of a car ")
        print(self.name)
        print(self.year)



bmw = Cars()    # First object 
mercedes = Cars()    # second object
audi = Cars()   # third object

bmw.show_details()