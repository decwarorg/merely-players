import math

class Planets:
    
    def __init__(self):
        pass
    
    def update(self, raw):
        rec = raw[3]
        tmp = rec.split('@ @')
        tmp1, tmp2 = tmp[1][:5], tmp[1][5:]
        tmp3 = tmp2.split(',')
        v = int(tmp3[0].strip())
        tmp4 = tmp3[1].split()
        h = int(tmp4[0].strip())
        vhd = [[v, h, int(math.sqrt(v ** 2 + h ** 2))]]
        return vhd
    
        