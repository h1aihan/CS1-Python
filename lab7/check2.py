def parse_line(string):
    L1=string.split('/',3)
    if len (L1)!=4:
        return None
    elif L1[0].isdigit()==False or L1[1].isdigit()==False or L1[2].isdigit()==False:
        return None    
    else:
        return L1[0],L1[1],L1[2],L1[3]
def get_line(fname,parno,lineno):
    f=open(fname)
    string=''
    list=[]
    for line in f:
        string+=line
        list=string.split('\n\n')
    a=1
    while a!=0:
        par=list[parno-1]
        par=par.split('\n')
        try:
            lin=par[lineno-1]
        except IndexError:
            parno+=1
            lineno=0
            continue
        if parse_line(lin)==None:
            lineno+=1
            continue
        else:
            a=0
            return lin
filenum=raw_input('Please file number ==> ')
filename=filenum+'.txt'
parno=int(raw_input('Please enter paragraph number ==> '))
lineno=int(raw_input('Please enter the line number ==>'))
print get_line(filename,parno,lineno)


        
        
