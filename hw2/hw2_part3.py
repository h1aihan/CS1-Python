Num1=int(raw_input("Enter a value ==> "))
print Num1 
def reverse(number):
    x=number/100
    y=(number-100*x)/10
    z=(number-100*x-10*y)
    number=int(str(z)+str(y)+str(x))
    return number
Num2=max(Num1,reverse(Num1))-min(Num1,reverse(Num1))
Num3=Num2+reverse(Num2)
print "\nHere is the computation:"
print max(Num1,reverse(Num1)),"-",min(Num1,reverse(Num1)),"=",Num2
print Num2,"+",reverse(Num2),"=",Num3
if Num3==1089:
    print "You see, I told you."
else:
    print"Are you sure your input is valid?"
