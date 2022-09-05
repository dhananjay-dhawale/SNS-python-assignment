#Dhananjay Dhawale

#Q4
#[Reduced  Residue  System  Modulo  m]  Given  an  
# integer  m,  output  the RRSM_m set of integers. 
# And also output the value of φ(𝑚), at end.

#12
#1 5 7 11 4

#method to compute gcd, euclidean algorithm to compute gcd
def computeGCD(x, y):
  while(y):
    x, y = y, x % y
  return abs(x)

n = int(input())

c = 0
for i in range(1, n):
  if(computeGCD(i, n) == 1):
    print(i, end = " ")
    c += 1
print(c)
