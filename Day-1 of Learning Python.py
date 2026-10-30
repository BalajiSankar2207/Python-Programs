BASICS OF PYTHON  PROGRAMS

1.Input and Output Practice:

 a=int(input())
b=float(input())
c=input()
d=int(input())
e=float(input())
print(a)
print(b)
print(c)
print(d)
print(e)
        
2.Progressive Float Execution

import struct
a=float(input())
a=struct.unpack('f',struct.pack('f',a))[0]
print("%.5f"%a)
print("%.4f"%a)
print("%.3f"%a)
print("%.2f"%a)
print("%.1f"%a)
print("%.0f"%a)

3.Sum, Difference, Product, Division and Modulo.

a,b=map(int,input().split())
print(a+b)
print(a-b)
print(a*b)
print(int(a/b))
if a<0 or b<0:
  mod=abs(a)%abs(b)
  print(-1*mod)
else:
  print(a%b)

4.ASCII

a=int(input())
print(chr(a))

5.Update Counter

a=int(input())
a=a+5
a=a*2
a=a-3
print(a)

6.ODD or EVEN

a = int(input())
print("Even" if a % 2 == 0 else "Odd")

7.Greatest Among Three Numbers

a = int(input())
b = int(input())
c = int(input())

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)

8Character Digit to Integer

a = int(input())
b = int(input())
c = int(input())

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)

9.Personalized Greeting

name = input()
print("Hi", name + ", welcome to the programming class!")

10.Calculate Total and Average Marks

name = input()
mark1 = int(input())
mark2 = int(input())
mark3 = int(input())
mark4 = int(input())
mark5 = int(input())
total = mark1 + mark2 + mark3 + mark4 + mark5
average = total / 5
print("Student Name:", name)
print("Total Marks:", total)
print("Average Marks: %.2f"%average)

11.Shape Area Calculation

area=int(input())
length=int(input())
breadth=int(input())
radius=int(input())
base=int(input())
height=int(input())
print("Area of Square=%d"%(area*area))
print("Area of Rectangle=%d"%(length*breadth))
print("Area of Circle=%.2f"%(3.14*radius*radius))
print("Area of Triangle=%d"%(int((0.5)*base*height)))

12.Shape Perimeter Calculation Program

a=int(input())
length=int(input())
width=int(input())
radius=int(input())
side1=int(input())
side2=int(input())
base=int(input())
print(4*a)
print(2*(length+width))
print("%.2f"%(2*3.14*radius))
print(side1+base+side2)

13.Handling Mixed Inputs

num = int(input())
sentence = input()
print(num)
print(sentence)




	




