#Dhananjay Dhawale
#Q2
#Extended Euclidean algorithm to output 𝑥,𝑦
#when 𝑎,𝑏is given, such 𝑎𝑥+𝑏𝑦=𝑔𝑐𝑑(𝑎,𝑏), where x<y.

# Euclidean Algorithm
# function for extended Euclidean Algorithm
 
 
def gcdExtended(a, b):
 
    # Base Case
    if a == 0:
        return b, 0, 1
 
    gcd, x1, y1 = gcdExtended(b % a, a)
 
    # Update x and y using results of recursive
    # call
    x = y1 - (b//a) * x1
    y = x1
 
    return gcd, x, y
 
 
# Driver code
a = int(input())
b = int(input())
g, x, y = gcdExtended(a, b)
print(x, y)
