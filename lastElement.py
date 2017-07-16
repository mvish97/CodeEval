#Mth to last element
file_In= open("sample.txt","r")
file1= file_In.readlines()
for obj in file1:
    index= len(obj)
    in1= eval(obj[index-2])
    print(obj[(index-2)-(in1*2)])
