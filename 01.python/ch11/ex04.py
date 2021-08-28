def flunk(s):
    return s < 60

score = [ 45, 89, 72, 53, 94 ]

for s in filter(flunk, score):
    print(s)

# a = flunk
# print(id(a), id(flunk))
# print(type(a), type(flunk))
# print(a)
# print(flunk)
