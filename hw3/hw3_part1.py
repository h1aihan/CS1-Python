##### Author: Han Hai
##### CS1 HW3_PART1
##### [team, games_played, win, draw, lose, goals for, goals against]
import hw3_util
teams = hw3_util.read_fifa()
id1=int(raw_input('Team 1 id => '))
print id1
id2=int(raw_input('Team 2 id => '))
print id2
team1=teams[id1]
team2=teams[id2]
point1=3*team1[2]+team1[3]
point2=3*team2[2]+team2[3]
goaldif1=team1[5]-team1[6]
goaldif2=team2[5]-team2[6]
print '\nTeam                Win   Draw  Lose  GF    GA    Pts   GD    '
print team1[0]+ ' '*(20-len(team1[0]))+ str(team1[2])+' '*(6-len(str(team1[2])))\
      +str(team1[3])+' '*(6-len(str(team1[3])))+str(team1[4])+' '*(6-len(str(team1[4])))\
      +str(team1[5])+' '*(6-len(str(team1[5])))+str(team1[6])+' '*(6-len(str(team1[6])))\
      +str(point1)+' '*(6-len(str(point1)))+str(goaldif1)+' '*(6-len(str(goaldif1)))
print team2[0]+ ' '*(20-len(team2[0]))+ str(team2[2])+' '*(6-len(str(team2[2])))\
      +str(team2[3])+' '*(6-len(str(team2[3])))+str(team2[4])+' '*(6-len(str(team2[4])))\
      +str(team2[5])+' '*(6-len(str(team2[5])))+str(team2[6])+' '*(6-len(str(team2[6])))\
      +str(point2)+' '*(6-len(str(point2)))+str(goaldif2)+' '*(6-len(str(goaldif2)))
if point1>point2:
    print '%s is better'%(team1[0])
elif point2>point1:
    print '%s is better'%(team2[0])
elif goaldif1>goaldif2:
    print '%s is better'%(team1[0])
elif goaldif2<goaldif1:
    print '%s is better'%(team2[0])
elif team1[5]>team2[5]:
    print '%s is better'%(team1[0])
elif team1[5]<team2[5]:
    print '%s is better'%(team2[0])
else:
    print 'Both teams are tied'
