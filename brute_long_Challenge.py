t=int(raw_input())
p=[]
for i in range(t):
    p.append(i)
def swap(arr, i, j):
    temp=arr[j]
    arr[j]=arr[i]
    arr[i]=temp
    return arr
count=[]
for i in range(len(p)):
    for j in range(len(p)):
        if(i!=j):
            t=swap(p,i,j)
            count.append(t)
di=[]
for i in count:
   i=tuple(i)
   di.append(i)
dict1={}
for i in di:
    if(i in dict1):
        dict1[i]+=1
    else:
        dict1[i]=1
max1=0
p1=0

for i in dict1:
    if(dict1[i]>max1):
        max1=dict1[i]
        p1=i

min1=10000000000
p2=0

for i in dict1:
    if(dict1[i]<min1):
        min1=dict1[i]
        p2=i

a=list(p1)
a = [x+1 for x in a]
b=list(p2)
b = [x+1 for x in b]
print ' '.join(map(str, a))
print ' '.join(map(str, b))

