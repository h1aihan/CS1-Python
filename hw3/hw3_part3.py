##### Author: Han Hai
##### CSCI HW3 part3 
##### Oct 8th 2015
##### a complicated code to print dimond
bchar=raw_input('Background char => ')
print bchar
fchar=raw_input('Foreground char => ')
print fchar
h=raw_input('Height => ')
print h
print ''
if h.isdigit()==False:
        print 'Please enter a number for height'
if len(bchar)>1:
        print 'Please enter one character for background'
if len(fchar)>1:
        print 'Please enter one character for foreground'
if h.isdigit()==True and len(bchar)==1 and len(fchar)==1:
        Height=int(h)
        i=1
        j=Height      
        while i<=Height/2:
                if i==3:
                        print str(i).rjust(len(str(Height)))+bchar*j+fchar+bchar*(2*i-2)+'o'+bchar*j
                else:
                        print str(i).rjust(len(str(Height)))+bchar*j+fchar+bchar*(2*i-2)+fchar+bchar*j
                i+=1
                j-=1
        if float(Height/2)==Height/2.:
                i-=1
                j+=1
                while Height/2<=i<=Height-1:
                        if i==3:
                                print str(i+1).rjust(len(str(Height)))+bchar*j+fchar+bchar*(2*(Height-i)-2)+'o'+bchar*j
                        else:
                                print str(i+1).rjust(len(str(Height)))+bchar*j+fchar+bchar*(2*(Height-i)-2)+fchar+bchar*j
                        i+=1
                        j+=1
        else:
                while Height/2<=i<=Height:
                        if i==3:
                                print str(i).rjust(len(str(Height)))+bchar*j+fchar+bchar*(2*(Height-i))+'o'+bchar*j
                        else:
                                print str(i).rjust(len(str(Height)))+bchar*j+fchar+bchar*(2*(Height-i))+fchar+bchar*j
                        i+=1
                        j+=1    
 