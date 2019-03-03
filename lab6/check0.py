sum = ''
for i in range(9):
    for j in range(9):
        if j==2 or j==5:
            sum+=str(i)+','+str(j)+'  '
        if j==8:
            if i==2 or i==5:
                sum+=str(i)+','+str(j)+'\n\n'
            else:
                sum+=str(i)+','+str(j)+'\n'
        elif j!=2 and j!=5 and j!=8:
            sum += str(i)+','+str(j)+' '
print sum