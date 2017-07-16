#Counting Primes
file= open("sample.txt","r")
file1= file.readlines()
file2= []
for obj in file1:
    temp = obj.split(",")
    file2.append(temp)


for obj in file2:
    temp2= obj[1].split() 
    end= eval(temp2[0]) #stores the limit
    initial= eval(obj[0]) #stores the initial point
    final=[]
    while(1):
        if(initial < end):
            initial+=1
            for j in range(2,initial,1):
                if(initial%j == 0):
                    temp3=0
                    break
                else:
                    temp3=1
            if(temp3 == 1):
                    final.append(initial)
                      
        else:
             break
    if(eval(obj[0]) < 3):
        print(len(final)+1)
    else:
        print(len(final))
