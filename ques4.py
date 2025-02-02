#Implement a `Student` class with a constructor that initializes `name` and `roll_number`. Write a method to return student details.

class Student:
    def __init__(self,name,roll_number):
        self.name=name
        self.roll_number=roll_number

    def student_details(self):
        ans=self.name+" "+self.roll_number
        return ans
    
name=input("Enter the name of the student: ")
roll_number=input(("Enter the roll number of the student: "))

st=Student(name,roll_number)
print(st.student_details())
        