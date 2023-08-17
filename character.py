ec = {
    "wolf": "狼人",
    "k_wolf": "狼王",
    "wk_wolf": "白狼王",
    "h_wolf": "隐狼",
    "s_wolf": "石像鬼",
    "b_wolf": "狼美人",
    "witch": "女巫",
    "hunter": "猎人",
    "prophet": "预言家",
    "guard": "守卫",
    "cupid": "丘比特",
    "d_hunter": "猎魔人",
    "bomber": "炸弹人",
    "knight": "骑士",
    "bear": "驯熊师",
    "wild_child": "熊孩子",
    "g_keeper": "守墓人",
}


class characher(object):
    def __init__(self, job, camp, love, alive, die_cause):
        self.job = job
        self.camp = camp
        self.love = love
        self.alive = alive
        self.die_cause = die_cause

    def __str__(self):
        if self.alive == 1:
            if len(ec[self.job]) == 2:
                return ec[self.job] + "  :\033[0;32m最终存活\033[0m"
            else:
                return ec[self.job] + ":\033[0;32m最终存活\033[0m"
        else:
            if len(ec[self.job]) == 2:
                return ec[self.job] + "  :\033[0;31m" + self.die_cause + "\033[0m"
            else:
                return ec[self.job] + ":\033[0;31m" + self.die_cause + "\033[0m"


class c_witch(characher):
    def __init__(self, save, kill):
        self.save = save
        self.kill = kill


wolf = characher("wolf", 0, 0, 1, -1)
k_wolf = characher("k_wolf", 0, 0, 1, -1)
wk_wolf = characher("wk_wolf", 0, 0, 1, -1)
h_wolf = characher("h_wolf", 0, 0, 1, -1)
s_wolf = characher("s_wolf", 0, 0, 1, -1)
b_wolf = characher("b_wolf", 0, 0, 1, -1)
witch = c_witch(1, 1)
witch.job, witch.camp, witch.love, witch.alive, witch.die_cause = "witch", 1, 0, 1, -1
hunter = characher("hunter", 1, 0, 1, -1)
prophet = characher("prophet", 1, 0, 1, -1)
guard = characher("guard", 1, 0, 1, -1)
cupid = characher("cupid", -1, 0, 1, -1)
d_hunter = characher("d_hunter", 1, 0, 1, -1)
bomber = characher("bomber", 1, 0, 1, -1)
knight = characher("knight", 1, 0, 1, -1)
bear = characher("bear", 1, 0, 1, -1)
wild_child = characher("wild_child", -1, 0, 1, -1)
g_keeper = characher("g_keeper", 1, 0, 1, -1)
