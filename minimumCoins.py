#Minimum coins
file_In= open("sample.txt","r")
file1= file_In.readlines()
file2= []
temp=0
initial=0
final=0
for obj in file1:
    file2.append(obj.split())
for obj in file2:
    temp=eval(obj[0])
    initial= temp%5 
    if(initial == 0):
        final= temp/5
    elif(initial == 1 or initial==3):
        final= temp//5 + 1
    elif(initial == 2 or initial==4):
        final= temp//5 + 2
    print(int(final))
    
        
    
    

    
