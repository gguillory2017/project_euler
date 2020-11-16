# Find the largest prime factor of 600851475143
# With minor alterations, this program will find the prime factorization of any number
import math
number = 600851475143 #input("Enter a number to be factorized. Only enter integers. Do not enter a prime number.\n")
store = number
#number = int(number)
primes = []
while number % 2 == 0:
    primes.append[2]
    number /= 2 
for i in range(3, math.floor(math.sqrt(number))):
    while number % i == 0:
        primes.append(i)
        number /= i
    i += 1

print("The prime factors of " +  str(store) + " are:  " + str(primes))

