#dictionary homework
#1-problem
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict.get("model"))
#2-problem
key="age"
print(key in thisdict)

#3-problem
print("number of keys in thisdict :",len(thisdict))

#4-problem
print("here is list of keys: ",list(thisdict.keys()))
#5-problem
print("here is list of values: ",list(thisdict.values()))
#6-problem
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
child1 = {
  "name" : "Emil",
  "year" : 2004
}
thisdict.update(child1)
print("here is the merged dict: ",thisdict)
#7-problem
thisdict.pop()
print(thisdict)

#8-problem
thisdict.clear()
print("here is emply dict: ",thisdict)
#9-problem
print(len(thisdict)==0)
print(len(child1)==0)
#10-problem
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
child1 = {
  "name" : "Emil",
  "year" : 2004
}
key="brand"
if key in thisdict:

      value=thisdict[key]
      print(key,value)
else:
      print("there is no such a key")
#11-problem
my_dict = {"apple": 1, "banana": 2}
my_dict["apple"] = 3  
print(my_dict) 
#12-PROBLEM
d = {
    "apple": 3,
    "banana": 5,
    "cherry": 5,
    "orange": 3
}

# Count how many times the value 3 appears
val = 3
count = sum(1 for v in d.values() if v == val)

print(count)
#13-problem
input_dict = {'a': 1, 'b': 2, 'c': 3}
newdict = {value: key for key, value in input_dict.items()}

print(newdict) 
#14-problem
d = {
    "apple": 3,
    "banana": 5,
    "cherry": 5,
    "orange": 3,
    "pear":5,
    "pineaple":4,
    "grape":5

}
newlist = []
key=5
if len(d)!=0:
    for i in d.keys:
        if d[i]==5:
                newdict.append(i)
    print("here is the list with the value of 5: ", newlist)
else:
      print("dict is empty")
#15-problem
k=list(map(input().split("enter keys' list")))
j=list(map(input().split("enter values' list")))
newdict={}
for key , value in zip(k,j):
      newdict[key]=value
print(newdict)
#16-problem
my_dict = {
    "name": "Alice",
    "details": {
        "age": 25,
        "city": "New York"
    },
    "active": True
}
y=0
for key, value in my_dict.items():
    if isinstance(value, dict):
        print(f"Nested dictionary found at key: '{key}'")
        y+=1
if y==0:
     print("Nested dictionary not found")
#17-problem
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily["child2"]["name"])
#18-problem
from collections import defaultdict
count = defaultdict(lambda: 5)

words = ["apple", "banana", "apple", "orange", "banana", "apple"]

for word in words:
    count[word] += 1

print(count)
#19-problem
todos = {'userId': 1, 'id': 1, 'title': 'A', 'completed': False,
     'completed': False,'userId': 1, 'id': 1, 'title': 'C', 'completed': False,
     'userId': 1, 'id': 2, 'title': 'A', 'completed': True,
     'userId': 2, 'id': 1,'title': 'B', 'completed': False}
res = []
for i in todos.values():
     if i not in res:
          res.append(i)
print(res)

#20-problem
d = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15}

myKeys = list(d.keys())
myKeys.sort()

sd = {i: d[i] for i in myKeys}
print(sd)


#21-problem
d = {'watermelon': 1, 'apple': 3, 'banana': 2}        
val_based = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}
print(val_based)

#22-problem
data = {
    "apple": 8,
    "banana": 7,
    "orange": 6,
    "grape": 3,
    "melon": 5
}


filtered_data = {k: v for k, v in data.items() if v >= 6}

print(filtered_data)

#23-problem
dict1 = {"apple": 1, "banana": 2, "orange": 3}
dict2 = {"grape": 4, "banana": 5, "melon": 6}

commonkeys = set(dict1.keys()) & set(dict2.keys())

if commonkeys:
    print("Common keys found:", commonkeys)
else:
    print("No common keys.")

#24-problem
data = (("apple", 3), ("banana", 5), ("orange", 2))

result = dict(data)

print(result)
#25-problem
data = {"apple": 3, "banana": 5, "orange": 2}

first_key = next(iter(data))
first_value = data[first_key]

print(f"First key: {first_key}, First value: {first_value}")



