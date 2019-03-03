def get_words(des):
    des=des.replace(',',' ').replace('.',' ').replace('.',' ').replace('()',' ').replace('"',' ').lower().split()
    list1=[]
    for i in des:
        if len(i)>=4:
            list1.append(i)
    s=set(list1)
    return s
f1=open(str(raw_input('==>'))+'.txt')
f2=open('allclubs.txt')
des1=''
file1=''
for i in f1:
    file1+=i
    des1+=i.split('|')[1]
similarity=[]
set1=get_words(des1)
for clubs in f2:1
    set2=get_words(clubs.split('|')[1])
    if clubs!=file1:
        num=len(set1&set2)
    similarity.append((num,clubs.split('|')[0]))
listsi=list(similarity)
listsi.sort(reverse=True)
top5=listsi[:5]
print 'The top 5 are %s'%(top5)
        
    