#Dhananjay Dhawale 
#Q1 
#print all common divisors in ascending order
#3 12 18 36
#1 2 3 6

#logic
#Find gcd of all numbers and then print its divisors

import math

# Method to print the divisors
def printDivisors(n):
    list = []

    # List to store half of the divisors
    for i in range(1, int(math.sqrt(n) + 1)):

        if n % i == 0:

            # Check if divisors are equal
            if n / i == i:
                print(i, end=" ")
            else:
                # Otherwise print both
                print(i, end=" ")
                list.append(int(n / i))

    # The list will be printed in reverse
    for i in list[::-1]:
        print(i, end=" ")


#method to compute gcd, euclidean algorithm to compute gcd
def computeGCD(x, y):
  while(y):
    x, y = y, x % y
  return abs(x)

#input number of elements
n = int(input())
arr = []

for i in range (0, n):
  #input arr elements
  ele = int(input())
  arr.append(ele)

#num will store gcd of all numbers of array
num = arr[0]
for i in range(1, n):
  num = computeGCD(num, arr[i])

#computing divisors of num
printDivisors(num)


