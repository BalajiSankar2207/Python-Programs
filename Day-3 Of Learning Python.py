Digit based problems challenges :

1.Count the number of digits

n=int(input())
if n==0:
  print("1")
else:
  count=0
  while n>0:
    n=n//10
    count+=1
print(count)

2.Sum of Even Digits

a=int(input())
even=0
while a>0:
  last=a%10
  if a%2==0:
    even+=last
  a=a//10
print(even)

3.Product of Digits

a=int(input())
digit=1 
while a!=0:
  last=a%10
  digit=last*digit
  a=a//10
print(digit)

4.Reverse a Number

n=int(input())
rev=0
while n>0:
  last=n%10
  rev=rev*10+last
  n=n//10
print(rev)

5.Palindrome Number

n=int(input())
temp=n
rev=0
while n>0:
  last=n%10
  rev=rev*10+last
  n=n//10
if rev==temp:
  print("Palindrome")
else:
  print("Not Palindrome")

6.First Digit of a Number

n=int(input())
while n>9:
  n=n//10
print(n)

7.Count Zeros in a Number

n=int(input())
count=0
if n==0:
  count=1
while n>0:
  last=n%10
  if last==0:
    count=count+1
  n=n//10
print(count)

8.Armstrong Number

 n=int(input())
temp=n
digit=0
while n>0:
  n=n//10
  digit+=1
n=temp
sum=0
while n>0:
  last=n%10
  sum=sum+last**digit
  n=n//10
if sum==temp:
  print("Armstrong")
else:
  print("Not Armstrong")

9.Strong Number

import math
n=int(input())
temp=n
r=0
res=0
while n>0:
  r=n%10
  res+=math.factorial(r)
  n//=10
if temp==res:
  print("Strong")
else:
  print("Not Strong")

10.Check Perfect Number

n=int(input())
sum=0
for i in range(1,n):
  if n%i==0:
    sum+=i
if sum==n:
  print("Perfect")
else:
  print("Not Perfect")