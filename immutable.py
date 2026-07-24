class Student:
    def __init__(self, roll, name):
        self.__roll = roll
        self.__name = name

    @property
    def roll(self):
        return self.__roll

    @property
    def name(self):
        return self.__name


s1 = Student(101, "Shouvik")

# s1.roll = 102
# s1.name = Rahul

print(s1.roll)
print(s1.name)

# s1.roll = 102    # Error
# s1.name = "Rahul" # Error