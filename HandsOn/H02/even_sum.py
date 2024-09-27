all = list(range(1, 1001))

total = 0

for num in all:
    if num % 2 == 0:
        total += num
print(total)

total = sum(range(2, 1001, 2))
print(total)

