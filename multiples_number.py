file = open('sample.txt')
file1 = file.readlines()
for obj in file1:
    temp = obj.split(',')
    x = int(temp[0])
    n = int(temp[1].strip())
    count = 1
    while True:
        if n*count > x:
            print(n*count)
            break
        else:
            count+=1
        
