w= int(raw_input("Width of box ==> ")) 
print str(w)
h=int(raw_input("Height of box ==> "))
print str(h)
c= str(raw_input("Enter frame character ==> "))
print c
strw= str(w)
strh= str(h)
lengw=len(strw)
lengh=len(strh)
print "\nBox:"
print c*w +("\n"+c+" "+strw+ "x"+ strh+ " "*(w-4-(lengw+lengh))+c)+ ("\n" +c+" "*(w-2)+c)*(h-3) + "\n"+c*w
