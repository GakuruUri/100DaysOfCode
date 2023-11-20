class Employee:
    # Common class base for all employees
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1 

        def displayCount(self):
            print("Total Employee %d" % Employee.empCount)

        def displayEmployee(self):
            print("Name: ", self.name, "Salary: ", self.salary)

emp1 = Employee ("Gregory", 75000)
emp2 = Employee ("Jennifer", 85000)
emp1.displayEmployee()
emp2.displayEmployee()

print ("Total EMployee %d" % Employee.empCount)
