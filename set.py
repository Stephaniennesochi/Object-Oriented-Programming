class employee:
    def __init__(self, Id, name, salary):
        self.Id = Id
        self.name = name
        self.__salary = salary
    def show(self):
        print(f"name: {self.name}, Id: {self.Id}, salary: {self.__salary}")
    def getsalary(self):
        return self.__salary
    def set_salary(self, amount):
        if amount > 5000:
            print("Invalid amount")
        else:
            self.__salary = amount
emp = employee ("0001","Ngozi",2000)
emp.show()
emp.set_salary(10000)
emp.show()
        