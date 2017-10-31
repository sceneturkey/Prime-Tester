#Tests a range of numbers and sorts the primes into a list

primes = []

print("Please enter 2 numbers to test between.")
y = int(input("First number:"))
z = int(input("Second number:"))
for x in range(y, z+1):
    is_prime = True
    if (x == 1 or x == 2):
        primes.append(x)
        continue
    elif (x % 2 == 0):
        continue
    for i in range(x, 1, -1):
        if (i == 2 and is_prime == True):
            print(x)
            continue
        elif (x % (i-1) == 0):
            is_prime = False
            continue
        else:
            continue

        
