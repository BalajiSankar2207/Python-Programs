String challenges :

1.Length of a string

s=input()
print(len(s))

2.Join the strings

S1=input()
S2=input()
print(S1+" "+S2)

3.Compare the Strings

s1 = input()
s2 = input()
if  s1 == s2:
  print("true")
else:
  print("false")

4. First character of a string

s=input()
print(s[0])


5.Last character of a string

s=input()
print(s[-1])

6.Join first & last characters of a string

s=input()
print(s[0]+s[-1])

7.s=input()
numcount=alphacount=False
for i in s:
  if i.isalpha():
    alphacount=True
  elif i.isdigit():
    numcount=True
  if alphacount and numcount:
    break
if alphacount and numcount:
  print("true")
else:
  print("false")

8.Uppercase check

s=input()
if s.isupper():
  print("true")
else:
  print("false")

9.Lowercase check

s=input()
if s.islower():
  print("true")
else:
  print("false")

10.String lengths equal or not

s1=input()
s2=input()
if len(s1)==len(s2):
  print("true") 
else:
  print ("false")

11.Reverse a string

s=input()
print(s[::-1])

12.Split strings by comma

s=input()
for i in s.split(","):
  print(i)

13.Remove vowels

string=input()
vow="aeiouAEIOU"
for char in string :
  if char in vow :
   string=string.replace(char,"")
print(string)    


14.Reverse the character case

s=input()
print(s.swapcase())

15.Print ascii value

s=input()
print(ord(s))

16.Remove occurrences of a char

s=input()
char=input()
print(s.replace(char,""))

17.Search for a word

sen=input()
word=input()
print("true" if word in sen else "false")

18.Count vowels and consonants

s=input()
vowcount=concount=0
for i in s:
  if i in "aeiouAEIOU":
    vowcount+=1 
  else:
    concount+=1 
    
print(vowcount)
print(concount)


19.Anagram check

s1=input().lower().replace(" ","")
s2=input().lower().replace(" ","")
if (len(s1)!=len(s2)):
  print("false")
elif sorted(s1)==sorted(s2):
  print("true")
else:
  print("false")

20.s=input()
if s==s[::-1]:
  print("true")
else:
  print("false")
			