# -*- coding: utf-8 -*-

import fileinput
import re

def repl(m):
    k = u = m.group(1)
    k = k.replace("ä","x")
    k = k.replace("ö","z")
    k = k.replace("Ä","X")
    k = k.replace("Ö","Z")
    return "\index{" + k + "@" + u + "}"

for x in fileinput.input():
    x = re.sub(".index\{.texttt\{([a-z_\\\\]+)\}\}", '\index{\\1@\\\\texttt{\\1}}', x)
    x = re.sub("\\\\index\{([a-zäöA-ZÄÖ0-9 ]+)\}", repl, x)
    print x,
#print
