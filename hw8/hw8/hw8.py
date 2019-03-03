import math
from Board import *
from Rick import *
if __name__=='__main__':
    f=open(raw_input('Board file name => '))
    r=open(raw_input('Rick file name => '))
    boardss=[]
    boards=[]
    rickss=[]
    ricks=[]
    obstacles=[]
    obstacless=[] 
    for line in f:
        boardss.append(line.strip('\n').split('|'))
    for line in r:
        rickss.append(line.strip('\n').split('|'))
    for i in boardss:
        boards.append(board(i[0],int(i[1]),int(i[2]),int(i[3]),i[4],i[5],i[6],i[7],map(int,i[8:])))
    for i in rickss:
        ricks.append(Rick(i[0],int(i[1]),int(i[2]),int(i[3]),float(i[4]),float(i[5]),boards))
    for board in boards:
        print board
    print '\nAll Ricks'
    for rick in ricks:
        print 'Time 0:',rick  
    print '---------------------------------------------------------------------------'
    time=1
    names=[]
    for rick in ricks:
        names.append(rick.boardname)
    set1=set(names)
    name2=[]
    while True:
        if len(ricks)==0:
            print '\n---------------------------------------------------------------------------'
            print'Time %d: Simulation ended'%(time-1)
            print''
            print'No Ricks were left alive!\n'
            print'The following Ricks were caught by Transdimensional Council of Ricks:'
            list3=list(set1)
            for name in list3:
                print '\tRick of %s'%(name)
            print '---------------------------------------------------------------------------'
            break
        if time==100:
            print '\n---------------------------------------------------------------------------'
            print 'Time 100: Simulation ended\n'
            for rick in ricks:
                rick.move()
                name2.append(rick.boardname)
            set2=set(name2)
            print 'The following Ricks are still alive:'
            for rick in ricks:
                print '\t',rick,'\n'
            print 'The following Ricks were caught by Transdimensional Council of Ricks:'
            if set2==set1:
                print 'No Ricks were caught by Transdimensional Council of Ricks'
            else:
                list3=list(set1-set2)
                for name in list3:
                    print '\tRick of %s'%(name)
            print '---------------------------------------------------------------------------'
            break    
        for rick in ricks:
            rick.move()
        for rick in ricks:           
            if rick.outofbound()==True:
                a= rick.__str__()
                info1, info2, info3= rick.changeboard()
                print '\nTime %d: %s'%(time, info1) 
                print '\tPast location: %s'%(a)
                print '\tCurrent location: Rick of %s is in %s board at (%d,%d) with speed (%.1f, %.1f)'%(rick.boardname, rick.board.name, info2, info3, rick.dx, rick.dy)
            if rick.crash()!=False:
                rick.reverse()           
                print '\nTime %d:'%(time), 'Rick of %s crashed into object at %s in %s board'%(rick.boardname,rick.crash(),rick.board.name)
                print '\tNew Speed is %.1f, %.1f'%(rick.dx, rick.dy)   
            for i in ricks:
                if rick.meet(i)==True:
                    print '\nTime %d: Rick of %s collided with Rick of %s in %s board'%(time,i.boardname, rick.boardname, rick.board.name)
                    rick.goback(i)
                    print  '\t',rick
                    print  '\t',i 
            if rick.stop()==True:
                print '\nTime %d: Rick of %s in %s board location (%d,%d) with speed magnitude %.1f stops.'%(time, rick.boardname, rick.board.name, rick.tLx, rick.tLy, (rick.dx**2+rick.dy**2)**0.5)
                ricks.remove(rick)            
        if (time+1)%10==0:
            print '\n---------------------------------------------------------------------------'
            print 'End of time %d: all free Ricks'%(time)
            for rick in ricks:
                print rick
            print '---------------------------------------------------------------------------' 
        time+=1

