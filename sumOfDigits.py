#sum of digits
file = open("sample.txt","r")
file1= file.readlines()
file2= []
for obj in file1:
    temp= obj.split()
    file2.append(temp[0])
for obj in file2:
    final = 0
    for i in range(len(obj)):
        final+= eval(obj[i])
    print(final)
