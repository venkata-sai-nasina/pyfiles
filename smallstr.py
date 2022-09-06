def SmallestString(s,c):
    i=0
    while(i<len(s)):
     if s[i]>c:
     s=s[:i]+c+s[:i]
     return s
    i=i+1
    s=s+c
    return s
S='abd'
C='c'
print(SmallestString(S,C))