# for y in range(1, 10):
#     for x in range(y):
#         print('*', end = '')
    # print()

# for y in range(1, 10):
#     for x in range(10 - y):
#         print('*', end = '')
#     print()


def print_star(begin, end):
    for y in range(begin, end):
        for x in range(y):
            print('*', end = '')
        print()

def print_star_rev(begin, end, diff = -1):
    for y in range(begin, end, diff):
        for x in range(y):
            print('*', end = '')
        print()

print_star(1, 10)
print()
print_star_rev(9, 0)
# print_star_rev(9, 0, -1)
