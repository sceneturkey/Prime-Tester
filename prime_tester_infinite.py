#Tests all numbers and prints all primes

primes = []
x = 0
while(True):
    x += 1
    is_prime = True
    if (x == 1 or x == 2):
        primes.append[x]
        print(x)
        continue
    elif (x % 2 == 0):
        continue
    for i in range(x, 1, -1):
        if (i == 2 and is_prime == True):
            primes.append[x]
            print(x)
            continue
        elif (x % (i-1) == 0):
            is_prime = False
            continue
        else:
            continue

        
