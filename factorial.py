import math
def factori(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*factori(n-1)
print(factori(4))
print(math.factorial(4))