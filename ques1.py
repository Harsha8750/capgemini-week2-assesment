# Create a class `Employee` with properties `name`, `id`, and `department`. Instantiate an object and assign values dynamically.

class Employee:
    def __init__(self,name,id,department):
        self.name=name
        self.id=id
        self.department=department

name=input("Enter the name of the employee:")
id=int(input("Enter the id of the employee:"))
department=input("Enter the department of the employee:")

emp=Employee(name,id ,department)

print(f'The name of the employee is {emp.name}')
print(f'The id of the employee is {emp.id}')
print(f'The department of the employee is {emp.department}')