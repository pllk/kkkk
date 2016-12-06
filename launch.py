from os import system

for x in range(1,30+1):
    u = str(x)
    if len(u) == 1:
        u = "0"+u
    u = "luku" + u + ".tex"
    system("python index.py < " + u + " > " + u + ".tmp")
    system("cp " + u + ".tmp " + u)
    system("rm " + u + ".tmp")
    print "ok",x
