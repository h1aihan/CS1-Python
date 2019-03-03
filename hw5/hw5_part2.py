####### Author: Han Hai
####### Oct 21 2015
####### HW5 part2
def winner(candidate1, candidate2, vote1,vote2):
    statewin1=int(candidate1[1])
    statewin2=int(candidate2[1])
    tiewin1=int(candidate1[2])
    tiewin2=int(candidate2[2])
    rep1=int(candidate1[3])
    rep2=int(candidate2[3])
    letter1=candidate1[0][0]
    letter2=candidate2[0][0]
    if vote1>vote2:
        score1=5*(statewin1+1)+2*(tiewin1)+int(.5*(rep1+vote1))
        score2=5*(statewin2)+2*(tiewin2)+int(.5*(rep2+vote2))
    elif vote1<vote2:
        score1=5*(statewin1)+2*(tiewin1)+int(.5*(rep1+vote1))
        score2=5*(statewin2+1)+2*(tiewin2)+int(.5*(rep2+vote2))
    elif vote1==vote2:
        score1=5*(statewin1)+2*(tiewin1+1)+int(.5*(rep1+vote1))
        score2=5*(statewin2)+2*(tiewin2+1)+int(.5*(rep2+vote2))
    if score1>score2:
        return letter1
    elif score1<score2:
        return letter2
    elif score1==score2:
        return '-'
def make_board(candidate1,candidate2):
    board=[]
    for i in range(5):
        for j in range(5):
            board.append(winner(candidate1, candidate2, j, i))
    return board
def print_board(board):
    print'Votes|  0    1    2    3    4  '
    print'-'*5+'|'+'-'*25
    print'  0  |  '+board[0]+' '*4+board[1]+' '*4+board[2]+' '*4+board[3]+' '*4+board[4]+'  '
    print'  1  |  '+board[5]+' '*4+board[6]+' '*4+board[7]+' '*4+board[8]+' '*4+board[9]+'  '
    print'  2  |  '+board[10]+' '*4+board[11]+' '*4+board[12]+' '*4+board[13]+' '*4+board[14]+'  '
    print'  3  |  '+board[15]+' '*4+board[16]+' '*4+board[17]+' '*4+board[18]+' '*4+board[19]+'  '
    print'  4  |  '+board[20]+' '*4+board[21]+' '*4+board[22]+' '*4+board[23]+' '*4+board[24]+'  '
if __name__ == "__main__":
    candidate1=raw_input('Enter candidate 1 stats ==> ')
    print candidate1
    candidate1=candidate1.split(',')
    candidate2=raw_input('Enter candidate 2 stats ==> ')
    print candidate2
    candidate2=candidate2.split(',')
    print "Columns are %s's votes, rows are %s's votes"%(candidate1[0],candidate2[0])
    board=make_board(candidate1,candidate2)
    print_board(board)
