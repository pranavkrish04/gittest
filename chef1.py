t=int(raw_input())
for i in range(t):
    N=int(raw_input())
    arr=map(int, raw_input().split(" "))
    even=[]
    odd=[]
    for j in range(len(arr)):
        if(arr[j]%2==0):
            even.append(arr[j])
        else:
            odd.append(arr[j])
    dict2={} #even
    dict1={} #odd
    for j in even:
        if(j in dict2):
            dict2[j]+=1
        else:
            dict2[j]=1

    for j in odd:
        if(j in dict1):
            dict1[j]+=1
        else:
            dict1[j]=1
    #calculating all combinations
    sum1=len(odd)*(len(odd)-1)/2
    sum2=len(even)*(len(even)-1)/2
    sub1=0
    sub2=0
    for j in dict1:
        if(dict1[j]>1):
            sub1+=(dict1[j]*(dict1[j]-1))/2
    for j in dict2:
        if(dict2[j]>1):
            sub2+=(dict2[j]*(dict2[j]-1))/2
    total=(sum1+sum2)-(sub1+sub2)
    #checking anomaly in even
    for j in dict2:
        if(j%4==0):
            if((4*(j/4))+2 in dict2):
                total-=dict2[j]*dict2[4*(j/4)+2]
    for j in dict1:
        if((j-1)%4==0):
            if(4*((j-1)/4)+3 in dict1):
                total-=dict1[j]*dict1[4*((j-1)/4)+3]
    print total