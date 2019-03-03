##### Author: Han Hai
##### HW4 PART2 LEGOS
##### Oct 15 2015
import hw4_util
legos = hw4_util.read_legos()
print 'Current legos %s'%(legos)
Type= raw_input('Type of lego wanted => ')
print Type
Quantity=int(raw_input('Quantity wanted => '))
print Quantity
if Type=='2x2':
    if legos.count('2x2')>=Quantity:
        legos.remove('2x2')
        print "I can use %d 2x2 legos for this"%(Quantity)
        print 'Remaining legos %s'%(legos)
    elif legos.count('2x1')>=2*Quantity:
        i=0
        while i<2*Quantity:
            legos.remove('2x1')
            i+=1
        print "I can use %d 2x1 legos for this"%(2*Quantity)
        print 'Remaining legos %s'%(legos)
    elif legos.count('1x1')>=4*Quantity:
        j=0
        while j<4*Quantity:
            legos.remove('1x1')
            j+=1
        print "I can use %d 1x1 legos for this"%(4*Quantity)
        print 'Remaining legos %s'%(legos)
    else:
        print "I don't have %d %s legos"%(Quantity,Type)
if Type=='2x1':
    if legos.count('2x1')>=Quantity:
        i=0
        while i<Quantity:
            legos.remove('2x1')
            i+=1
        print "I can use %d 2x1 legos for this"%(Quantity)
        print 'Remaining legos %s'%(legos)
    elif legos.count('1x1')>=2*Quantity:
        j=0
        while j<2*Quantity:
            legos.remove('1x1')
            j+=1
        print "I can use %d 1x1 legos for this"%(2*Quantity)
        print 'Remaining legos %s'%(legos)
    else:
        print "I don't have %d %s legos"%(Quantity,Type)
if Type=='1x1':
    if legos.count('1x1')>=Quantity:
            j=0
            while j<Quantity:
                legos.remove('1x1')
                j+=1
            print "I can use %d 1x1 legos for this"%(Quantity)
            print 'Remaining legos %s'%(legos)
    else:
            print "I don't have %d %s legos"%(Quantity,Type)        
        
        
    