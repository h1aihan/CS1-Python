name=(raw_input("Please enter a name ==> "))
print name
n70s=int(raw_input("Count in 1970 => "))
print str(n70s)
n80s=int(raw_input("Count in 1980 => "))
print str(n80s)
cn80s=100*(float(n80s)-n70s)/n70s
n90s=int(raw_input("Count in 1990 => "))
print str(n90s)
cn90s=100*(float(n90s)-n80s)/n80s
n00s=int(raw_input("Count in 2000 => "))
print str(n00s)
cn00s=100*(float(n00s)-n90s)/n90s

average=(cn80s+cn90s+cn00s)/3
line1="\nBabies named "+ name
print line1
print "*"*(len(line1)-1)+ "\n"
print "Year / Total / % change from previous decade"
print "1970 / "+str(n70s)
print "1980 / "+str(n80s)+" / %% %.2f"%(cn80s)
print "1990 / "+str(n90s)+" / %% %.2f"%(cn90s)
print "2000 / "+str(n00s)+" / %% %.2f"%(cn00s)
print "Average change: %% %.2f"%(average)



