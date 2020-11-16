#Find the smallest number that can be divided by the numbers 1 through 20 without a remainder
import time
start = time.time()
number = 20
isTarget = {False}
while(False in isTarget):
    isTarget = {True}
    for i in [11,12,13,14,15,16,17,18,19,20]:
         isTarget.add(True) if number % i == 0 else isTarget.add(False)
    if(False not in isTarget):
        break
    else:
        number +=20
end = time.time()

print("The smallest number that can be divided by the numbers 1 through 20 without a remainder is: " + str(number))
print("Ran in: " + str(end - start) + " seconds")

