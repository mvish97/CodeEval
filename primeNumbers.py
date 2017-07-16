#Prime Numbers
file= open("sample.txt","r")
file1= file.readlines()
file2= []
for obj in file1:
    temp= obj.split()
    file2.append(temp[0])

for obj in file2:
    i=2
    temp2= eval(obj)
    final=[2]
    initial= 0
    while(1):
        if(i < temp2):
            i+=1
            for j in range(2,i,1):
                if(i%j == 0):
                    initial=0
                    break
                else:
                    initial=1
            if(initial == 1):
                    final.append(i)
                      
        else:
             break
    for obj in final:
        if(final.index(obj) < len(final)-1):
            print(obj,end=",")
        else:
            print(obj)
        
        
