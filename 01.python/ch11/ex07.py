def add(s, b):
    return s + b

score = [45, 89, 72, 53, 94]
bonus = [2, 3, 0, 0, 5]

for s in map(add, score, bonus):
    print(s, end = ", ")
print()

def get_first_char(str):
    return str[0]

country = ['Korea', 'America', 'Iran', 'France', 'North korea']

print(list(map(get_first_char, country)))
