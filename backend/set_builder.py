def load_set():
    from Tshark import Tshark
    p=Tshark()
    f=open('sample.txt', 'a')
    proc=p.start('en0')
    for line in proc.stdout:
        f.write(str(line)+'\n')
    f.close()
