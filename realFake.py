#Real Fake
file_In= open("sample.txt","r")
file1= file_In.readlines()
final=""
for obj in file1:
    credit= ""
    final= obj.split()
    for obj2 in final:
        initial= 0
        initial2= 0
        temp=0
        credit+= obj2
        for i in range(0,len(credit),2):
            initial+= eval(credit[i])*2
        for j in range(1,len(credit),2):
            initial2+= eval(credit[j])
        temp= initial+initial2
    if(temp%10 == 0):
        print(True)
    else:
        print(False)
    
    
    

                       
            
    
        
    
