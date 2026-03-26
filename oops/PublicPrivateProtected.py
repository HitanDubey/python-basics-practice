class Employee:
    def __init__(self,name,salary):
        self.name = name
        self._salary = salary
    
    
    def display(self):
        return f"Name : {self.name}, Salary : {self._salary}"

class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department = department

    def display_manager(self):
        return f"Manager name : {self.name}  Department : {self.department}, Salary: {self._salary}" 


emp = Employee("Vipul",90000)
mgr = Manager("Himanshu",120000,"HR")

print(emp.display())
print(mgr.display_manager())
