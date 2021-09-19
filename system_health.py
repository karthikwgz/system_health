import subprocess as sp




def free_ram():
    mem = sp.Popen("free -m | grep ^Mem",shell=True,stdout=sp.PIPE).communicate()[0].decode("utf-8").split()
    total,used,free = mem[1],mem[2],mem[3]
    return total,used,free

def load_avg():
    ld = sp.Popen("cat /proc/loadavg",shell=True,stdout=sp.PIPE).communicate()[0].decode("utf-8")
    return ld

def hostname():
    hs = sp.Popen("hostnamectl status",shell=True,stdout=sp.PIPE).communicate()[0].decode("utf-8").split("\n")
    x = {k[0].strip():k[1].strip() for k in [a.split(":") for a in hs if ":" in a]}
    return x

def ps_count():
    psc = sp.Popen("ps aux | wc",shell=True,stdout=sp.PIPE).communicate()[0].decode("utf-8").split()
    return psc[0]

def up_time():
    up = sp.Popen("uptime -s",shell=True,stdout=sp.PIPE).communicate()[0].decode("utf-8")
    return up

def threshold():
    pass

