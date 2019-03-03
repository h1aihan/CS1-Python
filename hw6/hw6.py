###### Author: Han Hai
###### HW6
###### Date Nov 5
import textwrap
def get_villians():
    f=open('DrWhoVillains.tsv')
    list1=[]
    for i in f:
        list1.append(i.strip('\n').split('\t'))
    list2=[]
    list1.pop(0)
    for i in list1:
        list2.append((int(i[6]),i[0],i[8]))
    list2.sort(reverse=True)
    return list2
def print_villians(list2):
    print ''
    i=0
    while i<10:
        print str(i+1)+'.'+' %s'%(list2[i][1])
        i+=1
def find_other(idnum):
    list1=list2[idnum-1][2].split(',')
    listx=[]
    for i in list1:
        listx.append(i.strip())
    set1=set(listx)
    listcommon=[]
    set4=set1
    for i in list2:
        if i[1]!=list2[idnum-1][1]:
            list3=i[2].split(',')
            listy=[]
            for j in list3:
                listy.append(j.strip())
            set2=set(listy)
            set3=set1&set2
            set4=set4-set2
            if len(set3)!=0:
                listcommon.append(i[1].strip())
    listcommon.sort()
    list4=list(set4)
    list4.sort()
    return listcommon,list4
if __name__ == '__main__':
    list2=get_villians()
    a=1
    while a!=0:
        print_villians(list2)
        print "Please enter a number between 1 and 10, or -1 to end"
        valinput=raw_input('Enter a villain ==> ')
        print valinput
        if valinput.isdigit()==True:
            idnum=int(valinput)
            if 0<idnum<=10:
                share,unique=find_other(idnum)
                stringshare=''
                stringunique=''
                for i in share:
                    stringshare+=i+', '
                for j in unique:
                    stringunique+=j+', '
                stringshare=stringshare[:-2]
                stringunique=stringunique[:-2]
                stringshare=textwrap.wrap(stringshare,70)
                stringunique=textwrap.wrap(stringunique,70)
                print '%s in %d stories, with the following other villains:'%(list2[idnum-1][1],list2[idnum-1][0])
                print '=================================================='
                for k in stringshare:
                    print '\t'+k
                if len(unique)==0:   
                    print '\nThere are no stories with only this villain'
                    print '=================================================='    
                else:
                    print '\nThe stories that only features %s are:'%(list2[idnum-1][1])
                    print '=================================================='
                    for s in stringunique:
                        print '\t'+s
                    print ''
        else:
            if valinput=='-1':
                print 'Exiting'
                a=0  
            else:
                continue
    
    
        
    
    
    

    