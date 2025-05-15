#1-problem
s=input("enter username: ")
p=input("enter password: ")
s=s.replace(" ","")
p=p.replace(" ","")
print(s!="" and p!="")
#2-problem
a,b=map(int,input("enter two numbers: ").split())
if a==b:
    print("they are equal ")
else:
    print("they are not equal")
#3-problem
m=int(input("enter number: "))
t=m%2
if t==0:
    print("even")
else:
    print("not even ")
#4-problem
g,h,j=map(int,input("enter three numbers: ").split())
print(g!=h!=j)

#5-problem
s=input("input text: ")
d=input("input text: ")
print(len(s)==len(d))

#6-problem
n=int(input("enter number"))
print((n%3)==(n%5)==0)
#7-problem
o=int(input("enter the number: "))
oo=int(input("enter the next number: "))
print((o+oo)>50)
#8-problem
n=int(input("enter number"))
print((n>9) and (n<21))
