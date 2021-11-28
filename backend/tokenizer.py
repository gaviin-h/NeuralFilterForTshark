import math

def tokenize(line):
    vec=line.split()
    # j=u'→'.encode('utf-8')
    # while j in vec:
    #     vec.remove(j)
    vec=vec[1:]
    v=[vec[0]]
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
            l=int(n, 16)
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
    return math.log(prot)

def desc(d):
    re=''
    for n in d:
        for a in n:
            if (ord(a) > 96 and ord(a) < 123) or (ord(a)>64 and ord(a)<91) or (ord(a)>47 and ord(a)<58):
                re+=a
    return float(math.log(int(re, 36)))


one="1      0.000000 2601:643:c101:5700:d9b7:cdbd:725f:90b6    → 2607:f8b0:4005:80f::200a                   TLSv1.2     125     Application Data"
two="2      0.024935 2607:f8b0:4005:80f::200a                  → 2601:643:c101:5700:d9b7:cdbd:725f:90b6     TCP         86      443 → 52807 [ACK] Seq=1 Ack=64 Win=265 Len=0 TSval=4293138349 TSecr=916466552"
three="3    0.091029 192.168.0.37                              → 104.154.127.142                            TCP         66      52805 → 443 [ACK] Seq=1 Ack=12 Win=2047 Len=0 TSval=916466641 TSecr=3418831315"
four="4     0.090898 104.154.127.142                           → 192.168.0.37                               SSL         77      Continuation Data"
five="31    4.414333 2600:1901:1:c36::                         → 2601:643:c101:5700:107:ac91:b6c5:61f8      TLSv1.2     125     [TCP Spurious Retransmission] , Application Data"

print(tokenize(one))
print(tokenize(two))
print(tokenize(three))
print(tokenize(four))
print(tokenize(five))