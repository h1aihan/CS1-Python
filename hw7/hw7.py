import json
def find_stats(data, month):
    EMXT=[]
    EMNT=[]
    DT90=[]
    DX32=[]
    TPCP=[]
    TSNW=[]
    MNTM=[]
    avMNTM=[]
    MNTMall=[]
    for i in data:
        if i['month']==month:
            if i['EMXT']!=0 and i['EMXT']!=-9999:
                EMXT.append((i['EMXT'],i['year']))
            if i['EMNT']!=0 and i['EMNT']!=-9999:
                EMNT.append((i['EMNT'],i['year']))
            if i['DT90']!=0 and i['DT90']!=-9999:
                DT90.append((i['DT90'],i['year']))
            if i['DX32']!=0 and i['DX32']!=-9999:
                DX32.append((i['DX32'],i['year']))
            if i['TPCP']!=0 and i['TPCP']!=-9999:
                TPCP.append((i['TPCP'],i['year']))
            if i['TSNW']!=0 and i['TSNW']!=-9999:
                TSNW.append((i['TSNW'],i['year']))
            if i['MNTM']!=0 and i['MNTM']!=-9999:
                MNTM.append((i['year'],i['MNTM']))
                avMNTM.append(i['MNTM'])
    MNTM.sort()
    first10=MNTM[0:10]
    first=0
    average1=()
    for i in first10:
            first+=i[1]
    average1='%d-%d:'%(MNTM[0][0],MNTM[9][0]), first/len(first10)
    second10=MNTM[10:20]
    second=0
    average2=()
    for i in second10:
            second+=i[1]
    average2='%d-%d:'%(MNTM[10][0],MNTM[19][0]), second/len(second10)  
    third10=MNTM[20:30]
    third=0
    average3=()
    for i in third10:
            third+=i[1]
    average3='%d-%d:'%(MNTM[20][0],MNTM[29][0]), third/len(third10)    
    fourth10=MNTM[30:40]
    fourth=0
    average4=()
    for i in fourth10:
            fourth+=i[1]
    average4='%d-%d:'%(MNTM[30][0],MNTM[39][0]), fourth/len(fourth10)   
    fifth10=MNTM[40:50]
    fifth=0
    average5=()
    for i in fifth10:
            fifth+=i[1]
    average5='%d-%d:'%(MNTM[40][0],MNTM[49][0]), fifth/len(fifth10)    
    sixth10=MNTM[50:]
    sixth=0
    average6=()
    for i in sixth10:
            sixth+=i[1]
    average6='%d-%d:'%(MNTM[50][0],MNTM[-1][0]), sixth/len(sixth10)    
    average=sum(avMNTM)/len(avMNTM)
    MNTM.sort()
    sum1=0
    sum2=0
    for i in range(10):
        sum1+=MNTM[i][1]
    average10=sum1/10.
    MNTM.sort(reverse=True)
    for i in range(10):
        sum2+=MNTM[i][1]
    averagel10=sum2/10.
    EMXT.sort(reverse=True)
    EMNT.sort()
    DT90.sort(reverse=True)
    DX32.sort(reverse=True)
    TPCP.sort(reverse=True)
    TSNW.sort(reverse=True)
    stats=[]
    if len(EMXT)<3:
        stats.append('Not enough data')
    else:
        stats.append([EMXT[0],EMXT[1],EMXT[2]])
    if len(EMXT)<3:
        stats.append('Note enough data')
    else:
        stats.append([EMNT[0],EMNT[1],EMNT[2]])
    if len(DT90)<3:
        stats.append('Note enough data')
    else:
        stats.append([DT90[0],DT90[1],DT90[2]])
    if len(DX32)<3:
        stats.append('Note enough data')
    else:
        stats.append([DX32[0],DX32[1],DX32[2]])
    if len(TPCP)<3:
        stats.append('Note enough data')        
    else: 
        stats.append([TPCP[0],TPCP[1],TPCP[2]])
    TPCP.sort()
    if len(TPCP)<3:
        stats.append('Note enough data') 
    else:
        stats.append([TPCP[0],TPCP[1],TPCP[2]])
    if len(TSNW)<3:
        stats.append('Note enough data')
    else:
        stats.append([TSNW[0],TSNW[1],TSNW[2]])
    TSNW.sort()
    if len(TSNW)<3:
        stats.append('Note enough data')
    else:
        stats.append([TSNW[0],TSNW[1],TSNW[2]])
    stats.append(average)
    stats.append(average10)
    stats.append(averagel10)
    stats.append(average1)
    stats.append(average2)
    stats.append(average3)
    stats.append(average4)
    stats.append(average5)
    stats.append(average6)
    return stats
def print_stats(stats):
    print 'Temperatures'
    print '--------------------------------------------------'
    if len(stats[0])==3:
        print 'Highest max  value => %d: %.1f, %d: %.1f, %d: %.1f'%(stats[0][0][1],stats[0][0][0],stats[0][1][1],stats[0][1][0],stats[0][2][1],stats[0][2][0])
    else:
        print 'Highest max value => Not enough data'
    if len(stats[1])==3:
        print 'Lowest min value => %d: %.1f, %d: %.1f, %d: %.1f'%(stats[1][0][1],stats[1][0][0],stats[1][1][1],stats[1][1][0],stats[1][2][1],stats[1][2][0])
    else:
        print 'Lowest min value => Not enough data'   
    if len(stats[2])==3:
        print 'Highest days with max >= 90 => %d: %.1f, %d: %.1f, %d: %.1f'%(stats[2][0][1],stats[2][0][0],stats[2][1][1],stats[2][1][0],stats[2][2][1],stats[2][2][0])
    else:
        print 'Highest days with max >= 90 => Not enough data'
    if len(stats[3])==3:
        print 'Highest days with max <= 32 => %d: %.1f, %d: %.1f, %d: %.1f'%(stats[3][0][1],stats[3][0][0],stats[3][1][1],stats[3][1][0],stats[3][2][1],stats[3][2][0])
    else:
        print 'Highest days with max <= 32 => Not enough data'
    print ''
    print 'Precipitation'
    print '--------------------------------------------------'
    if len (stats[4])==3:
        print 'Highest total => %d: %.1f, %d: %.1f, %d: %.1f'%(stats[4][0][1],stats[4][0][0],stats[4][1][1],stats[4][1][0],stats[4][2][1],stats[4][2][0])
    else:
        print 'Highest total => Not enough data'
    if len(stats[5])==3:
        print 'Lowest total => %d: %.1f, %d: %.1f, %d: %.1f'%(stats[5][0][1],stats[5][0][0],stats[5][1][1],stats[5][1][0],stats[5][2][1],stats[5][2][0])
    else:
        print 'Lowest total => Not enough data'
    if len(stats[6])==3:
        print 'Highest snow depth => %d: %.1f, %d: %.1f, %d: %.1f'%(stats[6][0][1],stats[6][0][0],stats[6][1][1],stats[6][1][0],stats[6][2][1],stats[6][2][0])
    else:
        print 'Highest snow depth => Not enough data'
    if len(stats[7])==3:
        print 'Lowest snow depth => %d: %.1f, %d: %.1f, %d: %.1f'%(stats[7][0][1],stats[7][0][0],stats[7][1][1],stats[7][1][0],stats[7][2][1],stats[7][2][0])
    else:
        print 'Lowest snow depth => Not enough data'
    print ''
    print 'Average temperatures'
    print '--------------------------------------------------'
    print 'Overall: %.1f'%(stats[8])
    print 'First 10 years: %.1f'%(stats[9])
    print 'Last 10 years: %.1f'%stats[10]
    print ''
    print '%s '%(stats[11][0])+ '*'*int(stats[11][1])
    print '%s '%(stats[12][0])+ '*'*int(stats[12][1])
    print '%s '%(stats[13][0])+ '*'*int(stats[13][1])
    print '%s '%(stats[14][0])+ '*'*int(stats[14][1])
    print '%s '%(stats[15][0])+ '*'*int(stats[15][1])
    print '%s '%(stats[16][0])+ '*'*int(stats[16][1])
if __name__ == '__main__':
    month=int(raw_input('Enter a month (1-12) => '))
    print month
    data = json.loads(open("tempdata.json").read())
    stats= find_stats(data,month)
    print_stats(stats)
    
