print "please enter your first name"
first= str(raw_input())
length1=len(first)
print "please enter your last name"
last= str(raw_input())
length2=len(last+"!")
length3=len("Hello,")
length=max(length1,length2,length3) 
print "*"*(length+6)
print "** "+ "Hello,"+" "*(length-length3)+" "+"**"
print "** "+ first + " "*(length-length1)+" "+"**"
print "** "+ last + "!"+" "*(length-length2)+" "+"**"
print "*"*(length+6)