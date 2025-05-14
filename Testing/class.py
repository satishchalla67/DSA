
class Student:
    def __init__(self, firstName, lastName, email):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        
newStudent2=""
newStudent1 = Student('Satish', 'Challa', 'satishchalla67@gmail.com')
newStudent2 = newStudent1
print(newStudent2)