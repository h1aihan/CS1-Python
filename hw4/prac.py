#### Author: Han Hai
#### HW4 PART3 FLU DATA
#### OCT 15 2015
import hw4_util
country1=raw_input('First country => ')
print country1
country2=raw_input('Second country => ')
print country2
cdata1 = hw4_util.read_flu(country1)
print cdata1[24]
cdata2 = hw4_util.read_flu(country2)
if not cdata1:
    print 'I could not find country %s'%(country1)
if not cdata2:
    print 'I could not find country %s'%(country2)
elif len(cdata1)!=0 and len(cdata2)!=0:
    i=0
    sum1=0
    sum2=0
    max1=0
    max2=0
    while i<len(cdata1):
        sum1+=cdata1[i]
        sum2+=cdata2[i]
        if max1<cdata1[i]:
            max1=cdata1[i]
        if max2<cdata2[i]:
            max2=cdata2[i]
        i+=1
    average1=sum1/len(cdata1)
    average2=sum2/len(cdata2)
    cutoff1=(average1+max1)/2
    print cutoff1
    cutoff2=(average2+max2)/2
    print cutoff2
    print ''.ljust(12)+'1'.ljust(4)+'2'.ljust(4)+'3'.ljust(4)+'4'.ljust(4)+'5'.ljust(4)+'6'.ljust(4)\
          +'7'.ljust(4)+'8'.ljust(4)+'9'.ljust(4)+'10'.ljust(4)+'11'.ljust(4)+'12'.ljust(4)
    line1=''
    line2=''
    k=0
    while k<len(cdata1):
        if cdata1[k]>=cutoff1:
            line1+='+'
        if cdata1[k]<cutoff1:
            line1+='-'
        if cdata2[k]>=cutoff2:
            line2+='+'
        if cdata2[k]<cutoff2:
            line2+='-'
        k+=1
    print country1+' '*(12-len(country1))+line1
    print country2+' '*(12-len(country2))+line2
        