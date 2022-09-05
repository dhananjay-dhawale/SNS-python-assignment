#Dhananjay Dhawale

#Q5
#Given 𝑎,𝑥and 𝑛, output 𝑎𝑥(𝑚𝑜𝑑𝑛). Use fermat theorem 
# concept. Also print intermediate equations while computing, 
# in any readable form.

# 12412 124 151233121
# 44658604

def solve(a,x,n):
  temp1 = a
  temp2 = 1
  if x == 0:
      return temp2
  # num stores the binary reprenstation of the x in reverse
  num = bin(x)
  num = num[2:]
  num = num[::-1]

  # if x is odd
  if x&1:
      temp2 = temp1
  t = len(num)
  for i in range(1,t):
      temp1 = (temp1*temp1) % n
      if num[i] == '1':
          temp2 = (temp1*temp2)%n 
          #print(num[i],temp1,temp2)
  return temp2 

a = int(input())
x = int(input())
n = int(input())

# a^x mod n 
# if n is not prime solved normally
# else used fermat's theorem

res = solve(a, x, n)
print(res)

