# Find the sum of all primes below 2 million
target = 2000000
primes = [2]
x = 3

while x < target + 1:
    root = x **.5
    index = 0
    isComp = False
    while primes[index] <= root:
        isComp = True if x % primes[index] == 0 else False
        if(isComp):
            break
        index += 1
    if(not isComp):
        primes.append(x)
        x +=2
    else:
        x+=2

total = sum(primes)

print("The sum of all primes below " + str(target) + " is: " + str(total))


