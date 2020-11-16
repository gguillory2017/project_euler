#Find the sum of the even fibonacci terms bellow 4 million

first = 1
second = 2
term = first + second
sigma = 2
while(term < 4000000):
    term = first + second
    if(term % 2 == 0):
        sigma += term
    first = second
    second = term
    print("term: " + str(term))

print("The sum of even fibonacci terms below 4 million is: " + str(sigma))