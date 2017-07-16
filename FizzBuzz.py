#Fizz Buzz
final= ""
file_In= open("FizzBuzz.txt","r")
file1= file_In.readlines()
for i in range(len(file1)):
    file2= file1[i].split()
    for i in range (1,eval(file2[2])+1):
        if(i% eval(file2[0])==0 and i% eval(file2[1])==0):
            final+= "FB"+ " "
        elif(i% eval(file2[0]) == 0):
            final+= "F"+ " "
        elif(i% eval(file2[1])==0):
            final+= "B"+ " "
        else:
            final+= str(i)
    final+= "\n"
    file_In.close()
print (final)
