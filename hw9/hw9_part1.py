################# Han Hai
################# HW9
import json
import operator
f = open('businesses.json')
list=[]
a=0
businesses=[]
category=raw_input('Enter a category ==> ')
print category
cutoff=int(raw_input('Cutoff for displaying categories => '))
print cutoff
dict1={}
for line in f:
    business = json.loads(line)
    businesses.append(business)
for i in businesses:
    for j in i['categories']:
        dict1[j]=0
for i in businesses:
    if category in i['categories']:
        for j in i['categories']:
            if j!=category:
                dict1[j]+=1
sorted_dict=sorted(dict1.items(), key=operator.itemgetter(0))
for i in sorted_dict:
    if i[1]!=0:
        a=1
    if i[1]>=cutoff:
        list.append(i)
if a==0:
    print 'Searched category is not found'
elif len(list)==0:
    print 'None above the cutoff'
else:
    print 'Categories co-occurring with %s:'%(category)
    for i in list:
        print '%s: %d'%(i[0].rjust(30),i[1])
        
            
    