##### Author: Han Hai
##### CSCI1 HW3 part2
command=' '
i=0 
x=200
y=200
c=['','','','','']
direction='right'
print 'Turtle: (%d,%d) facing: %s'%(x,y,direction)
def move(x,y,direction,amount):
    if direction=='right':
        x+=amount
        return x,y 
    elif direction=='left':
        x-=amount
        return x,y
    elif direction=='up':
        y- =amount
        return x,y
    elif direction=='down':
        y+=amount
        return x,y
def turn(direction):
    if direction=='right':
        ndirection='up'
        return ndirection
    if direction=='left':
        ndirection='down'
        return ndirection
    if direction=='up':
        ndirection='left'
        return ndirection
    if direction=='down':
        ndirection='right'
        return ndirection
while i<5:
    command=raw_input('Command (move,jump,turn) => ')
    c[i]=command
    lowercommand=command.lower()
    if lowercommand=='move':
        print command
        location=move(x,y,direction,20)
        x,y=location
        print 'Turtle: (%d,%d) facing: %s'%(x,y,direction)
    elif lowercommand=='jump':
        print command
        location=move(x,y,direction,50)
        x,y=location
        print 'Turtle: (%d,%d) facing: %s'%(x,y,direction)
    elif lowercommand=='turn':
        print command
        direction=turn(direction)
        print 'Turtle: (%d,%d) facing: %s'%(x,y,direction)
    else:
        print command
        print 'Turtle: (%d,%d) facing: %s'%(x,y,direction)
    i+=1
print '\nAll commands entered %s'%(c)
c.sort()
print 'Sorted commands %s'%(c)