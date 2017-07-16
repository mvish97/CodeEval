#Decimal to Binary
file= open("sample.txt","r")
file1= file.readlines()
file2= []
for obj in file1:
    temp= obj.split()
    file2.append(temp[0])
for obj in file2:
    dividend=eval(obj)
    final= []
    while(dividend > 0):
        dividend= dividend//2
        final.append(dividend%2)
    for obj in final:
        print(obj,end="")
    print()
            
        
        
    
