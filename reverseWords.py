#Reverse Words
file= open("sample.txt","r")
file1= file.readlines()
file2= []
for obj in file1:
    file2.append(obj.split())
for obj in file2:
    for i in range(len(obj)-1,-1,-1):
        print(obj[i],end=" ")
    print()

        
