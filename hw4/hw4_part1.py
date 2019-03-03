#### Author: Han Hai
#### HW4 PART1 ALTERNATING WORDS
#### OCT 15 2015
a=raw_input('Enter a word => ')
print a
a=a.lower()
word=list(a)
def is_alternating(word):
    vowel=word[::2]
    consonent=word[1::2]
    i=0 
    j=0 
    k=0 
    x=0
    while i<len(vowel):
        if vowel[i]!='a' and vowel[i]!='e' and vowel[i]!='i' and vowel[i]!='o' and vowel[i]!='u':
            x+=1
        i+=1
    while j<len(consonent):
        if consonent[j]=='a' or consonent[j]=='e' or consonent[j]=='i' or consonent[j]=='o' or consonent[j]=='u':
            x+=1
        j+=1
    while k<len(consonent)-1:
        if consonent[k]>=consonent[k+1]:
            x+=1
        k+=1
    if len(word)<8:
        print "The word '%s' is not alternating"%(a)
    elif word[0]!='a' and word[0]!='e' and word[0]!='i' and word[0]!='o' and word[0]!='u':
        print "The word '%s' is not alternating"%(a)
    elif x!=0:
        print "The word '%s' is not alternating"%(a)
    else:
        print "The word '%s' is alternating"%(a)
is_alternating(word)
