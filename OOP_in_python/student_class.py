class Student:
    def __init__(self,name: str,age : int,grade:str):
        self.name = name 
        self.age = age
        self.grade = grade
    def display_info(self):
        print(f"\nStudent name is {self.name}\nAge is {self.age}\nGrade is {self.grade} ")

s1 = Student("Abhishek",21,"A++")
s2 = Student("ChatGPT",5,"O")
s1.display_info()
s2.display_info()