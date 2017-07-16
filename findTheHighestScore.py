#Find the highest score
file= open("sample.txt","r")
file1= file.readlines()
file2= []
for obj in file1:
    file2.append(obj.split("|"))
for obj in file2:
    for i in range(len(obj)):
        print(obj[i].split())
            
