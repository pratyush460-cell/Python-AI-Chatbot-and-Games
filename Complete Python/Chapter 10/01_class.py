class Employee: 
    language = "Py" # This is a class attribute
    salary = 1200000


Parle = Employee()
Parle.name = "Parle" # This is an instance attribute
print(Parle.name, Parle.language, Parle.salary)

patte = Employee()
patte.name = "Patte Roro Robinson"
print(patte.name, patte.salary, patte.language)

# Here name is instance attribute and salary and language are class attributes as they directly belong to the class