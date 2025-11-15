#Create a Person class where we will have five attributes and five behaviors.
# Make sure that each type of function is used, and I want you to also create the print
# function, which will print all the instance variable values.

class Person:

    def __init__(self):
        self.name = "Abhishek"
        self.age = 25
        self.height = "5.1 ft"
        self.weight = 66
        self.eye_color = "Black"

    def person_name(self):
        return self.name

    def person_age(self):
        return self.age

    def person_height(self):
        return self.height

    def person_weight(self):
        return self.weight

    def person_eye_color(self):
        return self.eye_color


obj_ref = Person()
print(obj_ref.person_name())
print(obj_ref.person_age())
print(obj_ref.person_height())
print(obj_ref.person_weight())
print(obj_ref.person_eye_color())