import random
import time
from cic.definitions import robots, Mode
from cic.robot.enemy_bases import EnemyBases
from cic.robot.enemy_ships import EnemyShips
from cic.robot.galaxy import Galaxy
from cic.robot.planets import Planets

class Brain:

    def __init__(self, name, braincnt, tc):
        self.name, self.braincnt, self.tc = name, braincnt, tc
        self.super = True if 'cic' in name else False
        self.listenlen = 1
        self.calmlen = 3
        self.last_new_ship_cnt = 0
        self.cnt = 0
        self.age = 0
        self.mode = Mode.defense
        self.age_offense = 25
        self.enemybases = EnemyBases()
        self.enemyships = EnemyShips()
        self.galaxy = Galaxy()
        self.planets = Planets()

    def next(self):
        self.backbrain()
        try:
            if self.super: self.super_()
            else: time.sleep(self.calmlen)
            if self.mode == Mode.offense: self.offense()
            elif self.mode == Mode.defense: self.defense()
        except:
            try: self.try_to_stay_in_game()
            except: raise
    
    def backbrain(self):
        self.cnt += 1
        self.age = self.cnt - self.last_new_ship_cnt
        if self.age > self.age_offense: self.mode = Mode.offense
    
    def super_(self):
        if self.age <= 2: self.command_and_response('*password *mink')
        self.speak()
        self.galaxy.ships(self.command_and_response('list ships', listenlen=2))
        if self.age % 2 == 0:
            self.galaxy.bases(self.command_and_response('list bases', listenlen=3))
        else:
            self.galaxy.planets(self.command_and_response('list planets', listenlen=3))
        self.galaxy.write()

    def offense(self):
        mode = 'normal'
        # res = self.command_and_response('time')
        res = self.command_and_response('bases enemy')
        targ = self.enemybases.update(res)
        if not targ[2]:
            res = self.command_and_response(f'li cl pl')
            targ = self.planets.update(res)
            mode = 'torp'
        if targ[2] > 6: self.approach(targ)
        else: self.attack(targ, mode)
            
    def defense(self):
        mode = 'normal'
        # res = self.command_and_response('time')
        res = self.command_and_response('list ships enemy')
        targ = self.enemyships.update(res)
        if not targ[2]:
            res = self.command_and_response(f'li cl pl')
            targ = self.planets.update(res)
            mode = 'torp'
        if targ[2] > 6: self.approach(targ)
        else: self.attack(targ, mode)

    def speak(self):
        if True:
            if self.name not in robots: return
            if random.uniform(0, 1) > .1: return
        msg = random.choice(robots[self.name])
        res = self.command_and_response(f'tell all; {msg}')

    def attack(self, targ, mode):
        if mode == 'torp':
            res = self.command_and_response(f'to r 3 {targ[0]} {targ[1]}')
        else:
            res = self.command_and_response(f'ph r {targ[0]} {targ[1]}')
            if random.uniform(0, 1) > .5: res = self.command_and_response(f'to r 2 {targ[0]} {targ[1]}')

    def approach(self, targ):
        dv = 0 if targ[0] == 0 else int(3 * targ[0] / abs(targ[0]))
        dh = 0 if targ[1] == 0 else int(3 * targ[1] / abs(targ[1]))
        tmp = random.uniform(0, 1)
        if tmp < .05: dv = 0; dh *= -1 # in case stuck
        elif tmp > .95: dh = 0; dv *= -1
        res = self.command_and_response(f'm r {dv} {dh}')
        # res = self.command_and_response(f'sc')

    def listen(self, secs):
        res, tmp = [], ''
        tf = time.time() + secs
        while time.time() < tf:
            try: tmp += self.tc.read_nonblocking(secs, timeout=.2).decode('utf-8')
            except: pass
        tmp = tmp.replace('\x07', '')  # \x07 is \xhh hex for \a escape seq for ascii bell
        for rec in tmp.strip().splitlines(): 
            if rec: print(rec) # log raw messages
        tmp = tmp.strip().lower().splitlines()
        for line in tmp:
            newshipsignals = ['set prompt', 'set ocdef', 'set output', 'reading commands', 'runs out']
            if any(x in line for x in newshipsignals):
                self.age = 0
                self.last_new_ship_cnt = self.cnt
            res.append(line)
        return res

    def command_and_response(self, command, listenlen=None):
        """send a command and get the response"""
        try:
            for _ in range(2): self.tc.sendline(); self.tc.expect('>', timeout=10)
            self.tc.sendline(command)
            if not listenlen: listenlen = self.listenlen
            res = self.listen(listenlen)
            # for rec in res:
            #     if rec: print(f'{self.cnt}|{self.age}|{rec}') # log formatted and lowered messages
            return res
        except: print(f"cmd exception '{command}'")

    def try_to_stay_in_game(self):
        for _ in range(2): self.tc.sendline(); self.tc.expect('>', timeout=10)  # try to stay in game
