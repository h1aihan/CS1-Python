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

def find_stories(name):
    list1=[]
    for i in list2:
        if i[1]==name:
            list1=i[2].split(',')
    listx=[]
    for i in list1:
        listx.append(i.strip())
    dict1=dict()
    print listx
    for i in listx:
        dict1.update({i:0})
    for i in listx:
        for j in list2:
            if j[1]!=list1[1]:
                list3=j[2].split(',')
                listy=[]
                for k in list3:
                    listy.append(k.strip())
                for h in listy:
                    if h==i:
                        dict1[i]+=1
    return dict1
def print_stories(dict1):
    print 'Stories featuring "%s"'%(name)
    print '----------------------------------'
    for key in dict1.keys():
        print '%s : %s'%(key,'*'*dict1[key])
        
if __name__ == '__main__':
    name=raw_input('Enter name of villain => ')
    print name+'\n'
    list2=get_villians()
    dict1=find_stories(name)
    print_stories(dict1)   