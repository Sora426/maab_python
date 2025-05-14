#list homework
#1-problem
k=list(map(input("enter list ").split()))
h=input("enter element")
print(k.count(h))
#2-problem
k=list(map(int,input("enter list ").split()))
print(sum(k))

#3-problem
k=list(map(int,input("enter list ").split()))
print(max(k))

#4-problem
k=list(map(int,input("enter list ").split()))
print(min(k))

#5-problem
k=list(map(input("enter list ").split()))
e=input("element: ")
print(e in k)


#6-problem
k=list(map(input("enter list ").split()))
if len(k)==0:
    print("the list is empty ")
else:

   print(k[0])

#7-problem
k=list(map(input("enter list ").split()))
if len(k)==0:
    print("the list is empty ")
else:

   print(k[-1])

#8-problem
k=list(map(input("enter list ").split()))
m=list(k[0],k[1],k[2])
print(m)
#9-problem
k=list(map(input("enter list ").split()))
p=k.reverse()
print(p)


#10-problem
k=list(map(input("enter list ").split()))
p=sorted(k)
print(p)

#11-problem
k=list(map(input("enter list ").split()))
print(list(set(k)))

#12-problem
k=list(map(input("enter list ").split()))
u=input("enter element: ")
i=input("enter index: ")
k[i]=u
print(k)

#13-problem
k=list(map(input("enter list ").split()))
u=input("enter element: ")
print(k.index(u))

#14-problem
k=list(map(input("enter list ").split()))
if not k:
    print(False)
else:
    print(True)

#15-problem
k=list(map(int,input("enter list ").split()))
o=0
for i in k:
    if i%2==0:
        o+=1
print("there are f{o} even numbers")

#16-problem
k=list(map(int,input("enter list ").split()))
o=0
for i in k:
    if i%2==1:
        o+=1
print("there are f{o} even numbers")

#17-problem
k=list(map(input("enter list ").split()))
m=list(map(input("enter list ").split()))
t=k.union(m)
print(t)

#18-problem
k=list(map(input("enter list ").split()))
m=list(map(input("enter sublist ").split()))
print(m in k)

#19-problem
k=list(map(input("enter list ").split()))
u=input("enter element: ")
i=input("enter another element you want to replace with: ")
t=k.index(u)
k[t]=i
print(k)

#20-problem
k=list(map(int,input("enter list ").split()))
print(sorted(k)[-2])

#21-problem
k=list(map(int,input("enter list ").split()))
print(sorted(k)[1])

#22-problem
k=list(map(int,input("enter list ").split()))
o=[]
for i in k:
    if i%2==0:
        o.append(i)
print("list cointain from even numbers: ",o)




#23-problem
k=list(map(int,input("enter list ").split()))
o=[]
for i in k:
    if i%2==1:
        o.append(i)
print("list cointain from odd numbers: ",o)

#24-problem
k=list(map(int,input("enter list ").split()))
print(len(k))

#25-problem
k=list(map(int,input("enter list ").split()))
m=k.copy()
print("there is copy list ",m)

#26-problem
k=list(map(input("enter list ").split()))
y=len(k)
if y%2==0:
    print(k[y//2-1],k[y//2])
else:
    print(k[y//2])
    
#27-problem
k=list(map(input("enter list ").split()))
s=input("starting index: ")
n=input("finishing index: ")
t=0
for i in range(s,n+1):
     if k[i]>t:
         t=k[i]
print("maximum number in sublist is ",t)

#28-problem
k=list(map(input("enter list ").split()))
s=input("starting index: ")
n=input("finishing index: ")
t=1e15
for i in range(s,n+1):
     if k[i]<t:
         t=k[i]
print("minimum number in sublist is ",t)

#29-problem
k=list(map(input("enter list ").split()))
s=input(  "index: ")
if abs(s)<k:
    k.remove(k[s])
print("final list:",k)

#30-problem
k=list(map(input("enter list ").split()))
m=k.copy()
print(k==sorted(m))

#31-problem
k=list(map(input("enter list ").split()))
n=input("enter the number: ")
o=[]
for i in k:
     o.append(n*i)
print(o)

#32-problem
k=list(map(input("enter list ").split()))
m=list(map(input("enter sublist ").split()))
o=sorted(k.union(m))

#33-problem
k=list(map(input("enter list ").split()))
target=input("input element: ")
indices = []
for i, item in enumerate(k):
        if item == target:
            indices.append(i)
print(indices)

#34-problem
k=list(map(input("enter list ").split()))
n = 2 
rotated_right = k[-n:] + k[:-n]
print("rotated list: ",rotated_right)

#35-problem
k=list(map(input("enter list ").split()))
s=input("starting index: ")
n=input("finishing index: ")
m=k[s,n]
print(m)

#36-problem
k=list(map(int,input("enter list ").split()))
summ=0
for i in k:
 if i>0:
     summ+=i 
print("sum of positive numbers=  ",summ)

#37-problem
k=list(map(int,input("enter list ").split()))
summ=0
for i in k:
 if i<0:
     summ+=i 
print("sum of negative numbers=  ",summ)

#38-problem
k=list(map(int,input("enter list ").split()))
is_palindrome = True  
i,j = 0, len(s) - 1
while i < j:
    if k[i] != k[j]:  
        is_palindrome = False
        break
    i += 1
    j -= 1

if is_palindrome:
    print("Yes , list is polidrom") 
else:
    print("No , list is not polidrom")

#39-problem
def create_nested_list(original_list, sublist_size):
    return [original_list[i:i + sublist_size] for i in range(0, len(original_list), sublist_size)]

original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sublist_size = 3
nested_list = create_nested_list(original_list, sublist_size)

print(nested_list)
#40-problem
k=list(map(input("enter list ").split()))
print(list(set(k)))
