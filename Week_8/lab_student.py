class LABStudent: 

# Constructor method

    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def introduce(self): # Method
        return f"Hi, I'm {self.name}, {self.age} years old, majoring in {self.major}."

    def study(self): # Method
       return f"{self.name} is studying {self.major}."