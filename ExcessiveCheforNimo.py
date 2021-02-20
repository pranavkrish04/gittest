t=int(raw_input())
for i in range(t):
    inn=map(int, raw_input().split(" "))
    N=inn[0]
    M=inn[1]
    X=inn[2]
    Y=inn[3]
    conditionX=0
    conditionY=0
    #four conditions
    if((N-1)%X==0 and (N-1)>0):
        conditionX=1
    elif((N-2)%X==0 and (N-2)>0):
        conditionX=2

    if((M-1)%Y==0 and (M-1)>0):
        conditionY=1
    elif((M-2)%Y==0 and (M-2)>0):
        conditionY=2

        flag=False
    #base condition
    if(N==1 and (M-1)%Y==0 and (M-1)>0):
        flag=True
    elif(N==2 and (M-2)%Y==0 and (M-2)>0):
        flag=True
    elif(M==1 and (N-1)%X==0 and (N-1)>0):
        flag=True
    elif(M==2 and (N-2)%X==0 and (N-2) >0):
        flag=True
    elif(M==2 and N==2):
        flag=True

    if(conditionX==1 and conditionY==1):
        flag=True
    elif(conditionX==2 and conditionY==2):
        flag=True
    if(flag):
        print "Chefirnemo"
    else:
        print "Pofik"