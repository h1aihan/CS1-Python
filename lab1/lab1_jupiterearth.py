pi=3.14
c=186000
Min= 60
distance_j=483632000.0
distance_e=92957100.0
diameter_j=88864.0
diameter_e=7926.0
volume_j= 4/3.0 * pi *diameter_j**3
volume_e=4/3.0 * pi * diameter_e**3
ratio1= distance_j / distance_e 
ratio2=volume_j / volume_e
timeS2j= distance_j / c  
timeS2e= distance_e/ c 
InttimeS2j= int(distance_j/c)
InttimeS2e= int(distance_e/c)
timeS2j_min= InttimeS2j/Min
timeS2e_min= InttimeS2e/Min
timeS2j_re= InttimeS2j%Min
timeS2e_re= InttimeS2e%Min

print "Jupiter is", ratio1, "times farther from the sun than the Earth is"
print"The volume of Jupiter is", ratio2, "times larger the the Earth is"
print "The time light travel from Jupiter to Sun is", timeS2j, "seconds"
print "The time light travel from Earth to Sun is",  timeS2e, "seconds"
print "The time light travel from Jupiter to Sun is about", InttimeS2j, "seconds"
print "The time light travel from Earth to Sun is about",  InttimeS2e, "seconds"
print "The time light travel from Jupiter to Sun is about", timeS2j_min, "minutes", timeS2j_re, "seconds"
print "The time light travel from Earth to Sun is about",  timeS2e_min, "minutes", timeS2e_re, "seconds"