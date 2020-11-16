#Find the sum of all numbers less than 1000 that are multiples of 3 or 5
sigma = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        sigma += i

print("The sum of all numbers less than 1000 that are multiples of 3 or 5 is: " + str(sigma))