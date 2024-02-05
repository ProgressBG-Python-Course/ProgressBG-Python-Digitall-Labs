# -------------------------- Dunder (magic) methods -------------------------- #
# class Person:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f'name: {self.name}; age: {self.age}'


# person1 = Person('Maria', 23)


# print(person1)
# print( person1.show_details() )

# --------------------------- Operator Overloading --------------------------- #
# class Person:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f'name: {self.name}; age: {self.age}'


#     def __sub__(self, other):
#         return self.age - other.age

# person1 = Person('Maria', 23)
# person2 = Person('Petar', 34)

# # print( person2.__sub__(person1) )
# print( person2 - person1 )


# ----------------------------------- TASKS ---------------------------------- #
# Find employee with the highest salary
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         # check for valid salary
#         if 0<=self.salary<=300_000:
#             self.salary = salary
#         else:
#             print('Invalid Salary Value')

#     def __str__(self):
#         return f'name: {self.name}; salary: {self.salary}'


# # employees = []
# # for _ in range(5):
# #     print('Enter Empoyee details:')
# #     name = input('Name: ')
# #     salary = input('Salary')

# #     employee = Employee(name, salary)
# #     employees.append(employee)

# employees = [
#     Employee("Ivan Petrov", 50000),
#     Employee("Maria Ivanova", 65000),
#     Employee("Mihail Georgiev", 48000),
#     Employee("Alisa Stoyanova", 52000),
#     Employee("Bogomil Nikolov", 70000)
# ]

# current_max_salaray = 0
# current_max_employee = None
# for employee in employees:
#     if employee.salary>=current_max_salaray:
#         current_max_salaray = employee.salary
#         current_max_employee = employee

# print(current_max_salaray)
# print(current_max_employee)


# -------------------------------- Inheritance ------------------------------- #
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        # check for valid salary
        if 0<=self.salary<=300_000:
            self.salary = salary
        else:
            print('Invalid Salary Value')

    def greet(self):
        print(f"I'm the employee {self.name}")

    def __str__(self):
        return f'name: {self.name}; salary: {self.salary}'

class Bulgarian:
    def greet(self):
        print("I'm Bulgarian")


class Manager(Employee, Bulgarian):
    def __init__(self, name, salary, department):
        # call parent constructor
        super().__init__( name, salary)
        self.department = department

    def greet(self):
        print(f"I'm Manager")
        # Bulgarian.greet(self)
        # super(Employee, self).greet()
        # super(Employee,self).greet()

manager1=Manager('Ivan', 30_000, 'Finance')
manager1.greet()


# ------------------------------- Encapsulation ------------------------------ #
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def change_balance(self, value):
        print('Log to DB...')
        self.__balance = value

    def __str__(self):
        return f"name: {self.name}, balance: {self.__balance}"


account1 = BankAccount('Maria', 5000)
account2 = BankAccount('Petar', 3000)


# account1._BankAccount__balance = 0
account1.change_balance(0)
print(account1)


