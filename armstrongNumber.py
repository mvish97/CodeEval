#Armstrong Numbers
file_In= open("sample.txt","r")
file1= file_In.read()
final= ""
file2=file1.split("\n")
for obj in file2:
    final=0
    exp = len(obj)
    if(exp > 0):
     for i in range(exp):
         final+= (eval(obj[i]))**(exp)
     if( final == eval(obj)):
         print (True)
     else:
         print(False)
            
        
        
    
