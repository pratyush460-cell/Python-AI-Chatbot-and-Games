class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")


parle = Employee()
# parle.language = "JavaScript" # This is an instance attribute
parle.greet()
parle.getInfo() 
# Employee.getInfo(parle)
 