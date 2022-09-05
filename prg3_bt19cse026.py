#Dhananjay Dhawale
#Q3
#[Fundamental  Theorem  of  Arithmetic]  Given  any  
# integer  output  the product of primes, in ascending order.
# If same prime appear multiple times then print it that 
# many times with spaces in between.

#20123122300 
#2 2 5 5 19 733 14449

n = int(input())
num = n

for i in range(2, n+1):
  while(num > 1 and num%i == 0):
    print(i, end = " ")
    num //= i
  if num == 1:
    break
  i += 1
