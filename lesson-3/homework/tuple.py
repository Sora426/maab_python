#hi
#1-problem
k=tuple(map(input("enter tuple: ").split()))
h=input("enter element")
print(k.count(h))
#2-problem
k=tuple(map(int,input("enter tuple: ").split()))
print(max(k))
#3-problem
k=tuple(map(int,input("enter tuple: ").split()))
print(min(k))
#4-problem
k=tuple(map(input("enter tuple: ").split()))
e=input("element: ")
print(e in k)
#5-problem
k=tuple(map(input("enter tuple ").split()))
if len(k)==0:
    print("the list is empty ")
else:
    print(k[0])
#6-problem
k=tuple(map(input("enter tuple ").split()))
if len(k)==0:
    print("the list is empty ")
else:
    print(k[-1])
#7-problem
k=tuple(map(input("enter tuple").split()))
print(len(k))
#8-problem
k=tuple(map(input("enter tuple ").split()))
m=tuple(k[0],k[1],k[2])
print(m)
#9-problem
k=tuple(map(input("enter list ").split()))
m=tuple(map(input("enter list ").split()))
t=k.union(m)
print(t)

#10-problem
k=tuple(map(input("enter list ").split()))
if k is True:
    print("tuple is not empty")
else:
    print("tuple is  empty")


#11-problem
k=tuple(map(input("enter tuple: ").split()))
u=input("enter element: ")
t=[]
for i in range(len(k)):
    if k[i]==u:
          t.append(i)

print("here is indices",t)

#12-problem
k=tuple(map(int,input("enter tuple ").split()))
print("here is second largest element ", sorted(k)[-2])

#13-problem
k=tuple(map(int,input("enter tuple ").split()))
print("here is second largest element ", sorted(k)[1])


#14-problem
k=tuple(input("enter element: "))
print("here is tuple that heve 1 element ", k)

#15-problem
k=list(map(input("enter list ").split()))
o=tuple(k)
print("here is tuple with same elements in lists ",o)

#16-problem
k=tuple(map(int,input("enter tuple ").split()))
o=sorted(k)
print(k==o)

#17-problem
k=tuple(map(input("enter list ").split()))
s=input("starting index: ")
n=input("finishing index: ")
t=0
for i in range(s,n+1):
     if k[i]>t:
         t=k[i]
print("maximum number in sublist is ",t)

#18-problem
k=tuple(map(input("enter tuple ").split()))
s=input("starting index: ")
n=input("finishing index: ")
t=1e15
for i in range(s,n+1):
     if k[i]<t:
         t=k[i]
print("minimum number in sublist is ",t)

#19-problem
k=tuple(map(input("enter tuple ").split()))
u=tuple(list(k)[1:])
print("here is your tuple ",u)

#20-problem
def create_nested_list(original_list, sublist_size):
    return [original_list[i:i + sublist_size] for i in range(0, len(original_list), sublist_size)]

original_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
sublist_size = 3
nested_tuple = tuple(create_nested_list(list(original_tuple), sublist_size))

#21-problem
k=tuple(map(input("enter list ").split()))
n=input("enter the number: ")
o=[]
for i in k:
     o.append(n*i)
o=tuple(o)
print(o)

#22-problem
k=tuple(map(input("enter list ").split()))
s=input("starting index: ")
n=input("finishing index: ")
m=tuple(k[s,n])
print(m)




#23-problem
k=tuple(map(input("enter list ").split()))
o=tuple(k[::-1])
print("here if reversed tuple: ",o)

#24-problem
k=tuple(map(input("enter list ").split()))
o=tuple(k[::-1])
print(k==o)

#25-problem
k=tuple(map(input("enter list ").split()))
r=tuple(set(k))
print("here is tuple with unique elements ", r)

    

