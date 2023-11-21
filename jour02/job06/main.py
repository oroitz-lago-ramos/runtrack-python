for i in range(2, 1001):
    isPrime = True
    for j in range(2, int(i ** 0.5) + 1):
        if ((i / j) == int(i / j)):
            isPrime = False
    if i == 2:
        print(i)
    elif (isPrime == True):
        print(i)