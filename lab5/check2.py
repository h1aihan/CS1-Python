import lab05_util
numid=int(raw_input('id of a restaurant==>'))-1
def print_info(restaurants):
    if -1<numid<156:
        print '%s (%s)'%(restaurants[0], restaurants[5])
        line3=restaurants[3].split('+')
        print '\t%s'%(line3[0])
        print '\t%s'%(line3[1])
        i=0        
        sum=0
        high=0
        low=1000
        while i<len(restaurants[6]):
            sum+=restaurants[6][i]
            if restaurants[6][i]>high:
                high=restaurants[6][i]
            if restaurants[6][i]<low:
                low=restaurants[6][i]
            if len(restaurants[6])<4:
                average=float(sum)/len(restaurants[6])
            if len(restaurants[6])>3:
                average=(float(sum)-high-low)/(len(restaurants[6])-2)
            i+=1
        if -1<average<=2:
            print 'This restaurant is rated bad, based on %d reviews.'%(len(restaurant[6]))
        if 2<average<=3:
            print 'This restaurant is rated average, based on %d reviews.'%(len(restaurants[6]))
        if 3<average<=4:
            print 'This restaurant is rated above average, based on %d reviews.'%(len(restaurants[6]))
        if 4<average<=5:
            print 'This restaurant is rated very good, based on %d reviews.'%(len(restaurants[6]))

    else:
        print 'invalid number'
restaurants=lab05_util.read_yelp('yelp.txt')
print_info(restaurants[numid])
    
