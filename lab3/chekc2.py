def coun_count(count_name, num_wins, num_losses, num_draw,goals_for,goals_against):
    points = num_wins * 3+num_draw
    goal_adv = goals_for - goals_against
    return "\n"+count_name+"\nWin: "+str(num_wins)+" Lose: "+str(num_losses)+" Draw: "+str(num_draw)+"\nTotal number of points: "+str(points)+" Goal advantage: "+str(goal_adv)
print coun_count("Germany",2,1,0,7,2)
print coun_count("USA",1,1,1,4,4)
print coun_count("Argentina",3,0,0,6,3)
print coun_count("England",0,1,2,2,4)