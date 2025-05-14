#hello
#1-problem
s=input("Name: ")
n=int(input("year of birth: "))
print(s , "is ",2025-n, "years old")
#2-problem
print("Malibu and Lasetti")
#3-problem
st=input("input text: ")
print(len(st),st.upper(), st.lower())
#4-problem
r=input()
is_palindrome = True  
i,j = 0, len(s) - 1
while i < j:
    if r[i] != r[j]:  
        is_palindrome = False
        break
    i += 1
    j -= 1

if is_palindrome:
    print("Yes") 
else:
    print("No")
#5-problem
s = input()
vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
u = sum(1 for ch in s if ch in vowels)
c=len(s)-u
print("Number of vowels:", u , "number of consonants: ", c)
#6-problem
str1 = input("enter text: ")

str2 = input("enter another text: ")

str3 = input("enter another text: ")

print(f'"{str1}" contains "{str2}" = {str2 in str1}')
print(f'"{str1}" contains "{str2.lower()}" = {str2.lower() in str1}')
print(f'"{str1}" contains "{str3}" = {str3 in str1}')

if str2 in str1:
    print(f'"{str1}" contains "{str2}"')
else:
    print(f'"{str1}" does not contain "{str2}"')
#7-problem
s=input("Input sentence: ")
r=input("replace: ")
w=input("With: ")
print(s.replace(r,w))
#8-problem
st=input("input text: ")
print(st[0],st[-1])
#9-problem
st=input("input text: ")
print(st[::-1])
#10-problem
s = input().split()
print(len(s))
#11-problem 
s = input()
print(s.isdigit())
#12-problem
l=list(map(int,input().split()))
print(",".join(l) )
#13-problem
s=input()
print(s.replace(" ",""))
#14-problem
s=input()
d=input()
print(s==d)
#15-problem
s = input().split()
for i in s:
    print(s[0], end="")
#16-problem
s=input()
d=input()
def remove(s, d):
  
  s = s.replace(d, "")

print(remove(s, d))
#17-problem
s= input("Enter a string: ")
symbol = input("Enter the replacement symbol: ")

vowels = "aeiouAEIOU"
for vowel in vowels:
    s = s.replace(vowel, symbol)

print("Modified string:", s)
#18-problem
s=input().split()
d=input()
m=input()
print(s[0]==d and s[-1]==m)





