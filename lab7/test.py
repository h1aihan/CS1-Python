f=open('1.txt')
list=[]
for line in f:
    list.append(line.split('\n'))
print list
    