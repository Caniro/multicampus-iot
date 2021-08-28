import random

for i in range(3):
    print(random.random())
print()
for i in range(3):
    print(random.randint(1, 10))
print()
for i in range(3):
    print(random.randrange(1, 10))
print()
for i in range(3):
    print(random.uniform(1, 10))

food = ["짜장면", "짬뽕", "탕수육", "군만두"]
print()
print(random.choice(food))
print()
print(random.sample(food, 2))
print()
print(food)
print()
random.shuffle(food)
print(food)
