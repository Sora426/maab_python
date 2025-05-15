#set homework
#1-problem
k=set(map(input("enter set: ").split()))
m=set(map(input("enter set: ").split()))
t=k.union(m)
print("here is new set contain unique elements in both set ",t)
#2-problem
k=set(map(input("enter set: ").split()))
m=set(map(input("enter set: ").split()))
t=k.intersection(m)
print("here is new set contain common elements in two set ",t)
#3-problem
k=set(map(input("enter set: ").split()))
m=set(map(input("enter set: ").split()))
t=k.difference(m)
print("here is new set  with elements from the first set that are not in the second. ",t)
#4-problem
k=set(map(input("enter set: ").split()))
m=set(map(input("enter set: ").split()))
t=k.issubset(m)
print("here is answer whether set k contain set m  ",t)
#5-problem
k=set(map(input("enter set ").split()))
u=input("enter element: ")
print("here is answer whether set contain that element   ",u in k)
#6-problem
k=set(map(input("enter set ").split()))
print("here is length of set  ",len(k))
#7-problem
k=list(map(input("enter list ").split()))
print("here is set contain unique elements   ",set(k))
#8-problem
k=set(map(input("enter set ").split()))
m=input("eneter element you want to remove ")
k.remove(m)
print("here is set without the element ",k)
#9-problem
k=set(map(input("enter set ").split()))
k.clear()
print("here is clear set:    ",k)

#10-problem
k=set(map(input("enter set ").split()))
print("set has element or elements: ",len(k)>0)


#11-problem
k=set(map(input("enter set: ").split()))
j=set(map(input("enter set: ").split()))
t=k.symmetric_difference(j)
print("here new set",t)

#12-problem
k=set(map(input("enter set ").split()))
s=input("enter element you want to add: ")
if s not in k: 
      k.add(s)
      print("here is new set with element s: ", k)
else:
     print("the element is already exist ,here is set: ", k)

#13-problem
k=set(map(input("enter set ").split()))
k.pop()
print("here is new set ",k )

#14-problem
k=set(map(int,input("enter set ").split()))
print("here maximum element ", max(k))

#15-problem
k=set(map(int,input("enter set ").split()))
print("here minimum element ", min(k))

#16-problem
k=set(map(int,input("enter set ").split()))
o=()
for i in k:
    if i%2==0:
        o.add(i)
print("set cointain from even numbers: ",o)

#17-problem
k=set(map(int,input("enter set ").split()))
o=()
for i in k:
    if i%2==1:
        o.add(i)
print("set cointain from odd numbers: ",o)

#18-problem
s=int(input("starting number: "))
n=int(input("finishing number: "))
n=()
for i in range(s,n+1):
         n.add(i)
print("here is new set of numbers between specific range ",n)

#19-problem
k=set(map(input("enter set: ").split()))
j=set(map(input("enter set: ").split()))
h=k.update(j)
print("here is your new set ",h)

#20-problem
k=set(map(input("enter set: ").split()))
j=set(map(input("enter set: ").split()))
h=k.isdisjoint(j)
print(h)





#21-problem
k=list(map(input("enter list ").split()))
n=list(set(k))

print("here is your list with unique elements: ",n)

#22-problem
k=list(map(input("enter  list: ").split()))

m=len(set(k))
print("here is number of unique elements",m)

#23-problem
import random

no = 10
a = 10 # start
b = 400 # end

res = random.choices(range(a, b + 1), k=no)
print(res)

