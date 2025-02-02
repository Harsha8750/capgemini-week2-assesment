#Create a multi-level class structure with `Person` → `Employee` → `Manager`,
#  where `Manager` has an additional method `approve_leave()`.

class Person:
    def __init__(self):
        pass
    def staff(self):
        print("Staff mainly works in the office")
    def client(self):
        print("clients give projects to the company")

class Employee(Person):
    def __init__(self):
        super().__init__()
    def dead_lines(self):
        print("The empoyee has to comlete the task given to him with in time")
    def shifts(self):
        print("Shifts may vary according to the requirement")

class Manager(Employee):
    def __init__(self):
        super().__init__()
    def work_allotment(self):
        print("The manager is responsible for allotment of work to employees")
    def approve_leave(self):
        print("The manager has to approve leave to the employee")

mn=Manager()
mn.work_allotment()
mn.approve_leave()