file_In= open("sample.txt","r")
file1= file_In.readlines()
file2= []
temp=0
for obj in file1:
    temp= obj.split()
    file2.append(temp[0])

for obj in file2:
    temp= eval(obj)
    seq= [1,1]
    if(temp > 2):
        for i in range(temp-2):
            seq.append(seq[(len(seq)-1)]+seq[len(seq)-2])
        print(seq[temp-1])
    elif(temp == 2 or temp == 1):
        print(1)
    else:
        print(0)
    
