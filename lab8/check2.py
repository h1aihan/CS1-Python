f1=open('ea.txt')
f2=open('wrpi.txt')
des1=''
des2=''
for i in f1:
    des1+=i.split('|')[1]
for i in f2:
    des2+=i.split('|')[1]

def get_words(des):
    des=des.replace(',',' ').replace('.',' ').replace('.',' ').replace('()',' ').replace('"',' ').lower().split()
    list1=[]
    for i in des:
        if len(i)>=4:
            list1.append(i)
    s=set(list1)
    return s
set1=get_words(des1)
set2=get_words(des2)
print 'Words in common %s'%(set1&set2)
print 'Words in file1 %s'%(set1-set2)
print set2-set1
