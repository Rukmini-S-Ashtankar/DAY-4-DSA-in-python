#==================   DEFAULT CONSTRUCTOR   ======================
# class Name:      #naming convention rule (N ame)
#     age = 30           #data member
#     def display(self):        #method
#         print("Hello World")

# obj = Name()
# print(obj.age)
# obj.display()

#===============================================================================
# class Student:                 # Constructor
#     def __init__(self):
#         self.name = "Rukmini"
#         self.age = 22

#     def display(self):
#      print("Name: ", self.name)
#      print("Age: ", self.age)
# stuObj = Student()                #without this two lines i wasn't getting any output
# print(stuObj)

#================================================================================
# class Message:
#    def __init__(self):
#       print("I am a Constructor")

#    def shows(self):
#       print("Class program")

# obj = Message()
# obj.shows()                 #this shows Class program statement
# obj2 = Message()

#================================================================================
#============     PARAMETERIZED CONSTRUCTOR     =====================

class StudentInfo:
    def __init__(self, name, age, roll_no):
        self.Name = name
        self.Age = age
        self.Rollno = roll_no

    def displayStudentInfo(self):
        print("Name=", self.Name)
        print("Age=", self.Age)
        print("Rollno=", self.Rollno)

studentObj = StudentInfo("Rukmini", 22, 25)
studentObj.displayStudentInfo()                                   # Got error