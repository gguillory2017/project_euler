#Find the largest palindromic number that is the product of two, 3 digit numbers

def reverse(s):
    rev = ""
    for i in range(len(s) -1 , -1, -1):
        rev += s[i]
    return rev

palindrome = []

for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        product = str(j * i)
        r = reverse(product)
        if product == r:
            palindrome.append(product)


palindrome = list(map(lambda n: int(n), palindrome))
palindrome.sort()
print("The largest product of two, 3 digit numbers is: " + str(palindrome.pop()))
        

