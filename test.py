a={0: {"x":-43,"y":154,"name":"Barny"}, 1: {"x":54,"y":-89,"name":"Marley"}}



maxv=[]
for i in range(0,len(a)):
        maxv.append(list(a[i].values())[0])


b=list(a[0].values())[0]

print(max(maxv))
print(list(a[0].values())[0])
print(list(a[1].values())[0])
