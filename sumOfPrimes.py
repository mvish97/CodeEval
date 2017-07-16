#Sum of primes
final= 2
count=0
i=0
while(1):
    if(count < 999):
        i+=1
        temp=0
        for j in range(2,i,1):
            if(i%j == 0):
                temp=0
                break
            else:
                temp=1
        if(temp == 1):
                final+=i
                count+=1
    else:
         break
print(final)
