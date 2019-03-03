print "please enter your first name"
first= str(raw_input())
length1=len(first)
print "please enter your last name"
last= str(raw_input())
length2=len(last+"!")
length3=len("Hello,")
length=max(length1,length2,length3) +2
print "*"*(length+5)
print "** "+ " "*((length-length3)/2)+"Hello,"+" "*((length-length3)/2)+"**"
print "** "+ " "*((length-length1)/2)+ first + " "*((length-length1)/2) +"**"
print "** "+ " "*((length-length2)/2)+ last + "!"+" "*((length-length2)/2)+"**"
print "*"*(length+5)