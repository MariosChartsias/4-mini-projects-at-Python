from collections import Counter
f = open("python5.txt", "r")
a= f.readlines()
f.close()
str1=""
for element in a:
    if element!='':
        str1+=element
str1=str1.replace('.','').replace(',','').lower()
a=str1.split()
b=Counter(a).most_common(10)
print("the 10 most displayed words are:\n",b)
c=[]
for element in a:
    if element[2:]!="":
        c.append(element[:2])
b=Counter(c).most_common(3)
print(2*'*******************************')
print("the 3 most displayed 2 first characters in all words are:\n",b)
c=[]
for element in a:
    if element[3:]!="":
        c.append(element[:3])
b=Counter(c).most_common(3)
print(2*'*******************************')
print("the 3 most displayed 3 first characters in all words are:\n",b)
