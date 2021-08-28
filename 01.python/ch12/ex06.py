import time
start = time.time()
for a in range(1000):
    print(a)
end = time.time()
print(end - start)

total = 0
start = time.time()
for num in range(100001):
    total += num
end = time.time()
print(end - start)
print(f"1 ~ 100000 = {total}")