f=open('ea.txt')
des=[]
for i in f:
    des=i.split('|')[1]
def get_words(des):
    des=des.replace(',',' ').replace('.',' ').replace('.',' ').replace('()',' ').replace('"',' ').lower().split()
    list1=[]
    for i in des:
        if len(i)>=4:
            list1.append(i)
    s=set(list1)
    return s
print get_words(des)



    
    
    

    
    