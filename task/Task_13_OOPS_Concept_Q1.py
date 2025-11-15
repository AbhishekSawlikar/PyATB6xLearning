class Person:
    # Class Attribute
    species = "Homo Sapiens"

    def __init__(self, name, age, gender, city, profession):
        # 5 Instance Attributes
        self.name = name
        self.age = age
        self.gender = gender
        self.city = city
        self.profession = profession

    # 1️⃣ Instance Method
    def introduce(self):
        return f"Hi, I am {self.name} from {self.city}. I work as a {self.profession}."

    # 2️⃣ Class Method
    @classmethod
    def get_species(cls):
        return f"All humans belong to: {cls.species}"

    # 3️⃣ Static Method
    @staticmethod
    def is_adult(age):
        return age >= 18

    # 4️⃣ Getter Method
    def get_age(self):
        return self.age

    # 5️⃣ Setter Method
    def set_age(self, new_age):
        if new_age > 0:
            self.age = new_age
        else:
            print("Age must be a positive number.")

    # Special Print Function (Magic Method)
    def __str__(self):
        return (
            f"Person Details:\n"
            f"Name       : {self.name}\n"
            f"Age        : {self.age}\n"
            f"Gender     : {self.gender}\n"
            f"City       : {self.city}\n"
            f"Profession : {self.profession}"
        )


# -------------------------------
# ✔ Creating an Object
# -------------------------------

p1 = Person("Abhishek", 29, "Male", "Mumbai", "QA Engineer")

# ✔ Calling Methods
print(p1.introduce())
print(Person.get_species())
print("Is adult:", Person.is_adult(p1.age))

# ✔ Using Getter & Setter
print("Age before update:", p1.get_age())
p1.set_age(30)

# ✔ Custom Print Function (__str__)
print("\n", p1)
