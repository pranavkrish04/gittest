t=int(raw_input())
import math
def isPerfectSquare(x): 
  
    # Find floating point value of  
    # square root of x. 
    sr = math.sqrt(x) 
   
    # If square root is an integer 
    return ((sr - math.floor(sr)) == 0) 
for i in range(t):
    inn=map(int, raw_input().split(" "))
    n=inn[0]
    q=inn[1]
    arr=map(int,raw_input().split(" "))
    for j in range(q):
        inn1=map(int,raw_input().split(" "))
        l=inn1[0]-1
        r=inn1[1]-1
        count=0
        
        for h in range(l,r+1):
            temp=arr[h]
            for g in range(h+1,r+1):
                temp= temp & arr[h] & arr[g]
                if(isPerfectSquare(temp)):
                    count+=1
        for h in range(l,r+1):
            if(isPerfectSquare(arr[h])):
                count+=1
        print count

