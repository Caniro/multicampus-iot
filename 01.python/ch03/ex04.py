print(ord('a'))
print(chr(98))

# for c in range('A', 'Z'):
#   print(chr(c), end='')
# print()

for c in range(ord('A'), ord('Z') + 1):
  print(chr(c), end='')
print()

for c in range(ord('A'), ord('Z') + 1):
  print(chr(c), c)
