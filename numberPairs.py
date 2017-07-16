#Number Pairs
file_In= open("sample.txt","r")
file1= file_In.readlines()
file2= [] 
file3= [] 
for obj in file1:
    file2.append(obj.split(";"))
for obj2 in file2:
    temp = obj2[1]
    if(file2.index(obj2) < len(file2)-1):
        file3.append(temp[0:len(temp)-1])
    else:
        file3.append(temp)
for k in range(len(file2)):
    temp= []
    temp2= file2[k] 
    temp= temp2[0].split(",") 
    final= []
    for i in range(len(temp)):
        for j in range(i+1,len(temp)):
            initial=0
            initial= eval(temp[i]) + eval(temp[j])
            if(initial == eval(file3[k])):
                final.append(temp[i]+","+temp[j])
    if(len(final) > 0):
        for obj3 in final:
            if( final.index(obj3) < len(final)-1):
                print(obj3, end=";")
            else:
                print(obj3)
    else:
        print("NULL")
            
            
            
        
    
                   
    
    
    
