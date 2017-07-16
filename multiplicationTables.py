#Multiplication tables

for i in range(1,13):
    final = ""
    for j in range(1,13):
        """if(j == 12):
            print(i*j)
        else:
            print(i*j, end= " ")"""
        """final.append(i*j)
    for obj in final:
        if(final.index(obj) == 11):
            print(obj)
        else:
            print(obj, end= "\t"*4)"""
        final+= str(i*j) + "    "
    print(final)
        
