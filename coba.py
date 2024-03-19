for i in range(1000):
    print(i)
    if i == 10:
        break
    
for i in range(1000):
    if i == 10:
        break
    print(i)

for i in range(10):
    if i == 5:
        continue
    print(i)
    
n = int(input("masukan n = "))
for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(i," ", end="")
    print()