class Human():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print(f"{self.age}살 {self.name}입니다.")

    def __str__(self):
        return f"<Human name: {self.name}, age: {self.age}>"

    def __repr__(self):
        return f"<Human name: {self.name}>"

kim = Human("김상형", 29)
kim.intro()
lee = Human("이승우", 45)
lee.intro()

print(kim)
print(lee)

li = [kim, lee]
print(li)

# object.__str__()
