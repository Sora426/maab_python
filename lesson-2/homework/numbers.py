#1-problem
n=float(input("enter the number: "))
print(round(n,2))
#2-problem
a=list(map(int,input().split()))
print("largest: ", max(a), "smallest: " ,min(a))
#3-problem
m=float(input())
print(m*1000 ,"meter", m*1000*100, "cm")
#4-problem
g,h=map(int,input().split())
print(g//h , g%h )
#5-problem
c=int(input("enter the temperuture in celsius: "))
print(c * (9/5) + 32)
#6-problem
f=int(input("enter the number"))
print("last degit of number is ", f%10)
#7-problem
o=int(input("enter the number: "))
if o%2==1:
    print("it is not even number")
else:
    print("it is even number")
