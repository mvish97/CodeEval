#Longest Lines
file_In= open("sample.txt", "r")
file1= file_In.readlines()
counter= []
final= []
for line in file1:
    counter.append(len(line))
for i in range(len(counter)):
    largest= max(counter)
    index= counter.index(largest)
    final.append(file1[index])
    counter[index]=0
for obj in final:
    print(obj)

    

