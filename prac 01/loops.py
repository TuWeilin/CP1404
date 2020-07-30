for i in range(1, 21, 2):
    print(i, end=' ')
print()

for num in range(0, 101, 10):
    print(num, end=' ')
print()

for num1 in range(20, 0, -1):
    print(num1, end=' ')
print()

n = int(input("Enter a num: "))
for n in range(1, n + 1):
    for j in range(n):
        print('*', end="")
    print()