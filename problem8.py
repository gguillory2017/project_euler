#Find the 13 digit number in the data file with the largest product.
file = open("data\problem8data.txt", "r")
numbers = file.read().replace('\n', "")

numSet = set()

for i in range(1000):
    tempNums = numbers[i:i+13]
    numSet.add(tempNums)

numSet = set(filter(lambda string: len(string) == 13, numSet))
numSet = set(filter(lambda string: string.find("0") == -1, numSet))

product = 0
nums = ""

for x in numSet:
    temp = 1
    for i in x:
        temp *= int(i)
    if(temp > product):
        product = temp
        nums = x

print("The 13 digit string with the largest product is: " + nums + ", and its product is: " + str(product))






