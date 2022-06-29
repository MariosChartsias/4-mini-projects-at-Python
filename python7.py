import json
from collections import Counter
f=open("python7.txt",'r')
a=f.readlines()
print("The available dictionaries are: ",end='')
dict={}
for i in range(0,len(a)):
    dict[i]=(json.loads(a[i]))
for i in range(0,len(list(dict[0].keys()))):
    if i!=0: print(end=',')
    print(list(dict[0].keys())[i],end=" ")
print('\n')
t=input("which of these keys are interested to you? ")
while t!='x' and t!='y' and t!='name':
    t=input("which of these keys are interested to you? ")

v=[]
if t=='x':
    p=0
elif t=='y':
    p=1
else:
    p=2
for i in range(0,len(dict)):
    v.append(list(dict[i].values())[p])
print(55*'*')
b=Counter(v).most_common(1)
print(f"The most popular value of {t} is {b[0][0]} which appears {b[0][1]} times")
print(f"minumum value of {t} is: ",min(v))
print(f"maximum value of {t} is: ",max(v))
