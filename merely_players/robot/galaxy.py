import json
import shutil
from merely_players.definitions import fed, emp

class Galaxy:
    
    def __init__(self):
        self.galaxy = {'ships': [], 'bases': [], 'planets': []}

    def planets(self, raw):
        if not raw: return 
        self.galaxy['planets'] = [] # reset
        for rec in raw:
            try:
                side = 'n'
                tmp = rec.split('@ @')
                tmp1, tmp2 = tmp[1][:5], tmp[1][5:]
                tmp3 = tmp1.split('-')
                v = int(tmp3[0].strip())
                tmp4 = tmp3[1].split()
                h = int(tmp4[0].strip())
                self.galaxy['planets'].append({'position': {'v': v, 'h': h}, 'side': side})
                # print(f'planets ok {str(tmp)}') #debug
            except:
                # print(f'planets except {str(tmp)}') #debug
                pass
        # for rec in self.galaxy['planets']: print(f'planets {rec}') # debug
        return
    
    def bases(self, raw):
        if not raw: return 
        self.galaxy['bases'] = [] # reset
        for rec in raw:
            try:
                tmp = rec.split('@')
                type = tmp[0].strip()
                if '<>' in type: side = 'f'
                elif ')(' in type: side = 'e'
                else: continue
                tmp1, tmp2 = tmp[1][:5], tmp[1][5:]
                tmp3 = tmp1.split('-')
                v = int(tmp3[0].strip())
                tmp4 = tmp3[1].split()
                h = int(tmp4[0].strip())
                self.galaxy['bases'].append({'position': {'v': v, 'h': h}, 'side': side})
                # print(f'bases ok {str(tmp)}') #debug
            except:
                # print(f'bases except {str(tmp)}') #debug
                pass
        # for rec in self.galaxy['bases']: print(f'bases {rec}') # debug
        return
        
    def ships(self, raw):
        if not raw: return 
        self.galaxy['ships'] = [] # reset
        for rec in raw:
            try:
                tmp = rec.split('@')
                name = tmp[0].strip()[-1]
                if name in fed: side = 'f'
                elif name in emp: side = 'e'
                else: side = 'r'
                tmp1, tmp2 = tmp[1][:5], tmp[1][5:]
                tmp3 = tmp1.split('-')
                v = int(tmp3[0].strip())
                h = int(tmp3[1].strip())
                self.galaxy['ships'].append({'position': {'v': v, 'h': h}, 'name': name, 'side': side})
            except: pass
        return
        
    def write(self):
        fp = open('data/galaxy.json', 'w')
        json.dump(self.galaxy, fp)
        fp.flush()
        fp.close()
        # try: shutil.copy('data/galaxy.json', '../galaxy/galaxy/galaxy.json')
        # except: pass
    