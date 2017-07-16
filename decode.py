#Challenge - Decode
file_In= open("sample.txt","r")
file1= file_In.readlines()
temp=""
final=""
for obj in file1:
    final=""
    for i in range(len(obj)):
        temp= ord(obj[i])+7
        final+= chr(temp)
    print(final)
        
