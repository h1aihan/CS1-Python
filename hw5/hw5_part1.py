####### Author: Han Hai
####### Oct 21 2015
####### HW5 part1
def next_pop(bpop, fpop):
    bpop_next = int(max(0,round((10*bpop)/(1+0.1*bpop) - 0.05*bpop*fpop)))
    fpop_next = int(max(0,round(0.4 * fpop + 0.02 * fpop * bpop)))
    return (bpop_next, fpop_next)
def check_convergence(bpop, fpop):
    next_pop(bpop,fpop)
    i=1
    a=0
    b=bpop,fpop
    pops=[a,b]
    converged=0
    while bpop!=0 and fpop!=0 and pops[i]!=pops[i-1] and i!=101:
        pops.append(next_pop(bpop,fpop))
        bpop,fpop=next_pop(bpop,fpop)
        i+=1
    if i==101:
        converged=False
    else:
        converged=True
    return bpop,fpop,i-1,converged
if __name__ == "__main__":
    bpop=int(raw_input('Please enter the starting bunny population ==> '))
    print bpop
    fpop=int(raw_input('Please enter the starting fox population ==> '))
    print fpop
    bpopf,fpopf,g,c=check_convergence(bpop,fpop)
    print '(Bunny, Fox): Start (%d, %d) End: (%d, %d), Converged: %s in %d generations'%(bpop,fpop,bpopf,fpopf,c,g)
