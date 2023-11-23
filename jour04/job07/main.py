L = [8, 24, 48, 2, 16]
count = 0
for i in range(0,len(L)):
    if L[i] % 3 == 0:
        count += 1
print(f"Il y a {count} multiples de 3 dans la liste")