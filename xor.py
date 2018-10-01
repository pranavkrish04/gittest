def prime_sieve(n):
    # returns all primes smaller than n
    sieve = [True] * n
    sieve[:2] = [False, False]  # 0 and 1 are not primes
    primes = []
    for prime, is_prime in enumerate(sieve):
        if not is_prime:
            continue
        primes.append(prime)
        for not_prime in range(prime*prime, n, prime):
            sieve[not_prime] = False
    return primes

def sum_of_primes(value):
    primes = prime_sieve(value)
    lo = 0
    hi = len(primes) - 1
    while lo <= hi:
        prime_sum = primes[lo] + primes[hi]
        if prime_sum < value:
            lo += 1
        else:
            if prime_sum == value:
                yield primes[lo], primes[hi]
            hi -= 1
#counting number of ones in binary no
def parity_checker(ar_in):
    counter=0
    for i in range(len(ar_in)):
        if((ar_in[i][0]%2==0 and ar_in[i][1]%2==0) or ar_in[i][0]%2!=0 and ar_in[i][1]%2!=0):
            counter+=1
            break
    return counter
t=int(raw_input())
for i in range(t):
    count_ans=0
    n=int(raw_input())
    arr=map(int, raw_input().split(" "))
    odd=[]
    even=[]
    for j in range(len(arr)):
        if(arr[j]%2==0):
            even.append(arr[j])
        else:
            odd.append(arr[j])
    for j in range(len(odd)):
        for h in range(len(odd)):
            if(j!=h and odd[j]!=odd[h]):
                check=list(sum_of_primes(odd[j]^odd[h]))
                if(check):
                    z=parity_checker(check)
                    if(z>0):
                        count_ans+=1
    for j in range(len(odd)):
        for h in range(len(odd)):
            if(j!=h and odd[j]!=odd[h]):
                check=list(sum_of_primes(odd[j]^odd[h]))
                if(check):
                    z=parity_checker(check)
                    if(z>0):
                        count_ans+=1


    print count_ans/2