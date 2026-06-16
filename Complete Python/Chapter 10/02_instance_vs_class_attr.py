class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000


parle = Employee()
parle.language = "JavaScript" # This is an instance attribute
print(parle.language, parle.salary)
 