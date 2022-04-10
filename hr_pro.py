
import datetime

from pkg_resources import working_set
class Employee:
   #Employee class here

    def __init__(self, name, age, salary, employment_year):
        self.name = name
        self.age = age
        self.salary = salary
        self.employment_year = employment_year

    def __str__(self):
        working_years = self.get_working_years()
        return f"Name: {self.name}, age: {self.age}, salary: {self.salary}, working_years: {working_years}"

    def get_working_years(self):
        today = datetime.date.today()
        working_years = int(today.year) - int(self.employment_year)
        return working_years


# ak = Employee('ak',29,2000,2018)
# print(ak)

class Manager(Employee):
    #Manager class here

    def __init__(self, name, age, salary, employment_year, bonus_percentage):
        Employee.__init__(self, name, age, salary, employment_year)
        self.bonus_percentage = bonus_percentage

    def __str__(self):
        working_years = self.get_working_years()
        bonus = self.get_bonus()
        return f"Name: {self.name}, age: {self.age}, salary: {self.salary}, working_years: {working_years}, bonus: {bonus}"

    def get_working_years(self):
        today = datetime.date.today()
        working_years = int(today.year) - int(self.employment_year)
        return working_years

    def get_bonus(self):
        bonus = self.bonus_percentage * self.salary
        return bonus

        
def main():
	# main code here
    employees = []
    managers = []
    print("Welcome to HR Pro 2022")
    print("Options:\n1. Show Employees \n2. Show Managers\n3. Add An Employee\n4. Add A Manager\n5. Exit")
    while True:
        todo = input("What would you like to do? ")
        print("---------------------------")
        match str(todo):
            case "1":
                for emp in employees:
                    print(emp)
            case "2":
                for mng in managers:
                    print(mng)
            case "3":
                name = input('Name: ')
                age = input('Age: ')
                salary = input('Salary: ')
                employment_year= input('Employement year: ')
                employees.append(Employee(name, age, salary, employment_year))
                print('Employee added succesfully')
            case "4":
                name = input('Name: ')
                age = input('Age: ')
                salary = input('Salary: ')
                employment_year= input('Employement year: ')
                bonus=input('Bonus Percentage: ')
                managers.append(Manager(name, age, salary, employment_year, bonus))
                print('Manager added succesfully')

            case "5":
                break
            case _:
                print("Wrong Input")
        if(todo == 5):
            break 

if __name__ == '__main__':
	main()
