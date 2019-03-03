bpop=int(raw_input("Number of bunnies ==> "))
fpop=int(raw_input("Number of foxes ==> "))
def cal_nextb(bpop,fpop):
    bpop_next = max(0,int((10*bpop)/(1+0.1*bpop) - 0.05*bpop*fpop))
    return bpop_next
def cal_nextf(bpop,fpop):
    fpop_next = max(0,int(0.4 * fpop + 0.02 * fpop * bpop))
    return fpop_next
print "Year 1:", bpop, fpop
print "Year 2:",cal_nextb(bpop,fpop),cal_nextf(bpop,fpop)
print "Year 3:",cal_nextb(cal_nextb(bpop,fpop),cal_nextf(bpop,fpop)), cal_nextf(cal_nextb(bpop,fpop),cal_nextf(bpop,fpop))
print "Year 4:",cal_nextb(cal_nextb(cal_nextb(bpop,fpop),cal_nextf(bpop,fpop)),cal_nextf(cal_nextb(bpop,fpop),cal_nextf(bpop,fpop))), cal_nextf(cal_nextb(cal_nextb(bpop,fpop),cal_nextf(bpop,fpop)),cal_nextf(cal_nextb(bpop,fpop),cal_nextf(bpop,fpop)))
print "Year 5:",cal_nextb(cal_nextb(cal_nextb(cal_nextb(bpop,fpop),cal_nextf(bpop,fpop)),cal_nextf(cal_nextb(bpop,fpop),cal_nextf(bpop,fpop))),cal_nextf(cal_nextb(cal_nextb(bpop,fpop),cal_nextf(bpop,fpop)),cal_nextf(cal_nextb(bpop,fpop),cal_nextf(bpop,fpop)))), cal_nextf(cal_nextb(cal_nextb(cal_nextb(bpop,fpop),cal_nextf(bpop,fpop)),cal_nextf(cal_nextb(bpop,fpop),cal_nextf(bpop,fpop))),cal_nextf(cal_nextb(cal_nextb(bpop,fpop),cal_nextf(bpop,fpop)),cal_nextf(cal_nextb(bpop,fpop),cal_nextf(bpop,fpop))))