def parse_line(string):
    L1=string.split('/',3)
    if len (L1)!=4:
        return None
    elif L1[0].isdigit()==False or L1[1].isdigit()==False or L1[2].isdigit()==False:
        return None    
    else:
        return L1[0],L1[1],L1[2],L1[3]
print parse_line("12/a/412/3/4/Here is some random text, like 5/4=3")
