def has_number(raw,colum,bd):
    if 0<=raw<9and 0<=colum<9:
        if bd[raw][colum].isdigit()==True:
            return True
        else:
            return False
    else:
        return True
def ok_to_add(number,raw, colum,bd):
    violation=0
    for a in range(9):
        for b in range(9):
            if a==raw and bd[a][b].isdigit()==True and int(bd[a][b])==number:
                violation+=1
            if b==colum and bd[a][b].isdigit()==True and int(bd[a][b])==number:
                violation+=1
    print violation
    if raw<=2:
        if colum<=2:
            r1=0
            r2=3
            c1=0
            c2=3
        if 2<colum<=5:
            r1=0
            r2=3
            c1=3
            c2=6
        if 5<colum<=9:
            r1=0
            r2=3
            c1=6
            c2=9
    if 2<raw<=5:
        if colum<=2:
            r1=3
            r2=6
            c1=0
            c2=3
        if 2<colum<=5:
            r1=3
            r2=6
            c1=3
            c2=6
        if 5<colum<=9:
            r1=3
            r2=6
            c1=6
            c2=9
    if 5<raw<=9:
        if colum<=2:
            r1=6
            r2=9
            c1=0
            c2=3
        if 2<colum<=5:
            r1=6
            r2=9
            c1=3
            c2=6
        if 5<colum<=9:
            r1=6
            r2=9
            c1=6
            c2=9
    print r1,r2,c1,c2
    for c in range(r1,r2):
        for d in range (c1,c2):
            if bd[c][d].isdigit()==True and int(bd[c][d])==number:
                violation+=1
    print violation
    if violation!=0:
        return False 
    if violation==0:
        return True
              
bd = [ [ '1', '.', '.', '.', '2', '.', '.', '3', '7'],
       [ '.', '6', '.', '.', '.', '5', '1', '4', '.'],
       [ '.', '5', '.', '.', '.', '.', '.', '2', '9'],
       [ '.', '.', '.', '9', '.', '.', '4', '.', '.'],
       [ '.', '.', '4', '1', '.', '3', '7', '.', '.'],
       [ '.', '.', '1', '.', '.', '4', '.', '.', '.'],
       [ '4', '3', '.', '.', '.', '.', '.', '1', '.'],
       [ '.', '1', '7', '5', '.', '.', '.', '8', '.'],
       [ '2', '8', '.', '.', '4', '.', '.', '.', '6'] ]
def print_bd(bd):
    sum=''
    for i in range(9):
        for j in range(9):
            if j==0:
                sum+='|'+' '+bd[i][j]
            if j==2 or j==5:
                sum+=' '+bd[i][j]+' '+'|'
            if j==8:
                if i==2 or i==5 or i==8:
                    sum+=' '+bd[i][j]+' '+'|'+'\n'+(len(bd)*2+7)*'-'+'\n'
                else:
                    sum+=' '+bd[i][j]+' '+'|''\n'
            elif j!=0 and j!=2 and j!=5 and j!=8:
                sum += ' '+bd[i][j]
    print (len(bd)*2+7)*'-'
    print sum
raw=int(raw_input('Enter raw ==> '))-1
colum=int(raw_input('Enter colum ==> '))-1
number=int(raw_input('Enter a number ==>'))
if ok_to_add(number,raw,colum,bd)==True and has_number(raw,colum,bd)==False:
    bd[raw][colum]=str(number)
    print_bd(bd)
else:
    print 'This number cannot be added'
