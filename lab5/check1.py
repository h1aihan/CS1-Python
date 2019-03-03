import lab05_util
def print_info(restaurants):
    print '%s (%s)'%(restaurants[0], restaurants[5])
    line3=restaurants[3].split('+')
    print '\t%s'%(line3[0])
    print '\t%s'%(line3[1])
    i=0
    sum=0
    while i<len(restaurants[6]):
        sum+=restaurants[6][i]
        i+=1
    average=float(sum)/len(restaurants[6])
    print 'average Score:%.2f'%(average)
restaurants=lab05_util.read_yelp('yelp.txt')
print_info(restaurants[1])
