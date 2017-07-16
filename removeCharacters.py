#Remove Characters
def main():
    file_In= open("sample.txt", "r")    
    file1= file_In.readlines()
    temp= [0,0,0]
    final= ""
    for obj in file1:
        temp1= obj.split(",") #list that contains the seperated line
        remove = temp1[1] #holds the letters that have to be omitted 
        temp[0]= remove[1]
        temp[1]= remove[2]
        temp[2]= remove[3]
        ch = temp1[0]
        for i in range(len(temp1[0])):
                if(ch[i] is temp[0] or ch[i] is temp[1] or ch[i] is temp[2]):
                       final+=""
                else:
                       final+= ch[i]
        final+="\n"
    print(final)
main()
