import math

def tokenize(line):
    vec=line.split()
    vec=vec[2:-2]
    v=[]
    v.append(addr(vec[1]))
    v.append(addr(vec[3]))
    v.append(prot(vec[4]))
    v.append(float(vec[5]))
    v.append(desc(vec[6:]))
    return v 

def addr(a):
    if '.' in a:
        r=a.split('.')
        re=''
        for c,n in enumerate(r):
            if c<3:
               re+=n
            else:
                re+='.'+n
        return float(re)
        
    else:
        r=a.split(':')
        while '' in r:
            r.remove('')
        re=''
        a=0
        d=0
        for c,n in enumerate(r):
            try:
                l=int(n, 16)
            except ValueError:
                l=0
                for i in n:
                    l+=int(ord(i))
            if c<4:
                a+=l
            else:
                d+=l
        re=str(a)+'.'+str(d)
        return float(re)
        
def prot(p):
    prot=0
    for i in p:
        prot+=ord(i)
    return float(prot)

def desc(d):
    re='1'
    for n in d:
        for a in n:
            if (ord(a) > 96 and ord(a) < 123) or (ord(a)>64 and ord(a)<91) or (ord(a)>47 and ord(a)<58):
                re+=a
    return float(math.log(int(re, 36)))