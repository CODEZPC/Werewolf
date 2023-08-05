class characher(object):
    def __init__(self,job,camp,love,alive,die_cause):
        self.job = job
        self.camp = camp
        self.love = love
        self.alive = alive
        self.die_cause = die_cause
    def __str__(self):
        if self.alive == 1:
            return self.job + ":最终存活"
        else:
            return self.job + ":" + self.die_cause
class c_witch(characher):
    def __init__(self,save,kill):
        self.save = save
        self.kill = kill
wolf = characher("wolf",0,0,1,-1)
k_wolf = characher("k_wolf",0,0,1,-1)
wk_wolf = characher("wk_wolf",0,0,1,-1)
h_wolf = characher("h_wolf",0,0,1,-1)
s_wolf = characher("s_wolf",0,0,1,-1)
b_wolf = characher("b_wolf",0,0,1,-1)
witch = c_witch(1,1)
witch.job,witch.camp,witch.love,witch.alive,witch.die_cause = "witch",1,0,1,-1
hunter = characher("hunter",1,0,1,-1)
prophet = characher("prophet",1,0,1,-1)
guard = characher("guard",1,0,1,-1)
cupid = characher("cupid",-1,0,1,-1)
d_hunter = characher("d_hunter",1,0,1,-1)
bomber = characher("bomber",1,0,1,-1)
knight = characher("knight",1,0,1,-1)
bear = characher("bear",1,0,1,-1)
wild_child = characher("wild_child",-1,0,1,-1)
g_keeper = characher("g_keeper",1,0,1,-1)