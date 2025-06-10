class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
    
    def introduce(self): 
        print(f"Hi, I'm {self.name} and I'm {self.age}.")

class Student(Person):
    def __init__(self, name, age, disipline, std_id, level):
        super().__init__(name, age) 
        self.disipline = disipline
        self.std_id = std_id
        self.level = level
    def info (self):
        print(f"{self.std_id} {self.name} is a student of Aptech Computer Education, studying {self.disipline} currently in level {self.level}")

std1 = Student("Devinton", 29, "Software Engineering", "std123", 4)
std2 = Student("Oluchi", 22, "Data Structure & Algorithm", "std124", 2)
std3 = Student("Zippora", 25, "Data Analysis", "std125", 3)

print(std1.introduce())
print(std2.info())
print(std3.info())

#Polymophism
class Employer:
    def work(self):
        print("Working...")
class Manager(Employer):
    def work(self):
        print("Manage teams and meetings..")

class Developer(Employer):
    def work(self):
        print("Working on the companies codebase.")

class Anlyst(Employer):
    def work(self):
        print("Analyzing some data for system model.")
class Intern(Employer):
    def work(self):
        print("Working on an interface of the company app.")
def company_day(employer: Employer):
    employer.work()

employers = [Manager(), Developer(), Anlyst(), Intern()]

for emp in employers:
    company_day(emp)


str = "World Best"
itr = iter(str)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))

