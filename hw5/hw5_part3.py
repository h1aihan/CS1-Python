####### Author: Han Hai
####### Oct 21 2015
####### HW5 part3
def openfiles(filename):
    names=[]
    for line in open(filename):
        line = line.strip("\n")
        names.append(line.split(','))
    return names
def find_top(a,number):
    fname=[]
    mname=[]
    topfname=[]
    topmname=[]
    for i in range(len(a)):
        a[i].reverse()
        a[i][0]=int(a[i][0])
    a.sort(reverse=True)
    for i in range(len(a)):
        if a[i][1]=='F':
            b=a[i][2],str(a[i][0])
            fname.append(b)
        if a[i][1]=='M':
            b=a[i][2],str(a[i][0])
            mname.append(b)
    for i in range(number):
        topfname.append(fname[i])
        topmname.append(mname[i])
    return topfname, topmname 
def print_name(topfname,topmname):
    print 'Top female names'
    a=''
    for i in range(len(topfname)):
        if float((i+1)/3)==(i+1)/3. and (i+1)/3!=0:
            a+=topfname[i][0]+' ('+topfname[i][1] + ')\n'
        else:
            a+=topfname[i][0]+' ('+topfname[i][1] + ') '
    print a.strip()
    print 'Top male names'
    b=''
    for i in range(len(topmname)):
        if float((i+1)/3)==(i+1)/3. and (i+1)/3!=0:
            b+=topmname[i][0]+' ('+topmname[i][1] + ')\n'
        else:
            b+=topmname[i][0]+' ('+topmname[i][1] + ') '
    print b.strip()
if __name__ == "__main__":
    files=raw_input('File name => ')
    print files
    a=openfiles(files)
    number=int(raw_input('How many names to display? => '))
    print str(number)+'\n'
    topfname,topmname=find_top(a,number)
    print_name(topfname,topmname)
    
      