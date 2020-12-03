import math
from collections import Counter
import time
answer = 0
index = 1
found_answer = False
start = time.time()
while(not found_answer):
    triangularNumber = (index * (index + 1))/2
    number = triangularNumber
    store = number
    primes = []
    while number % 2 == 0:
        primes.append(2)
        number /= 2 
    for i in range(3, int(math.sqrt(number))+1,2):
        while number % i == 0:
            primes.append(i)
            number /= i
    if number > 2:
        primes.append(int(number))
    d = dict(Counter(primes))
    divisors = 1
    for x,y in d.items():
        divisors *= y+1
    if divisors > 500:
        found_answer = True
        answer = int(store)
        print("Answer is: " + str(answer) + "|||index is: " + str(index))
    index += 1
end = time.time()
print("Ran in: " + str(end - start) + " seconds")



