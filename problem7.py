# Find the 10001st prime number
import time
whichPrime = input("Which prime number would you like to see? (Enter 1 for first, 2 for second, ... ,50 for 50th etc)\n")
whichPrime = int(whichPrime)
primes = [2]
i = 3
start = time.time()
while len(primes) < whichPrime + 1:
    root = i ** .5
    index = 0
    isComp = False
    while primes[index] <= root:
        isComp = True if i % primes[index] == 0 else False
        if(isComp):
            break
        index += 1
    if(not isComp):
        primes.append(i)
        i +=2
    else:
        i+=2
end = time.time()
print("Prime number " + str(whichPrime) + " is: " + str(primes[len(primes) - 2]))
print("Finished in " + str(end - start) + " seconds")

