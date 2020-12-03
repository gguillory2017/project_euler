#Find the difference between the square of the sum and the sum of the squares for the first 100 numbers
import time
number = input("Upper bound?\n")
number = int(number)
choice = input("Brute force method or the closed form method?\na. brute force\nb. closed form\n")

def sumOfTerms(x):
    return (x**2+x)/2

def sumOfSquares(x):
    return (x*(x+1)*(2*x+1))/6


if choice == "a":
    print("brute force")
    print("__________________")
    start = time.time()
    squareOfSum = 0
    sumOfSquares = 0
    for i in range(1,number + 1):
        squareOfSum+=i
        sumOfSquares+=i**2
    difference = squareOfSum**2 - sumOfSquares
    end = time.time()
    print("The difference between the square of the sum and the sum of squares for the first " + str(number) + " numbers is: " + str(difference))
    print("Completed in: " + str(end - start) + " seconds")
if choice =="b":
    print("closed form")
    print("__________________")
    start = time.time()
    difference = sumOfTerms(number)**2 - sumOfSquares(number)
    end = time.time()
    print("The difference between the square of the sum and the sum of squares for the first " + str(number) + " numbers is: " + str(difference))
    print("Completed in: " + str(end - start) + " seconds")






