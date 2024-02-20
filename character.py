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


def ch(n, c):
    eval(n).job = n
    eval(n).camp = c


class character(object):
    def __init__(self, job, camp, love=0, alive=1, die_cause=-1):
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

    def show(self):
        return ec[self.job]


class killer(character):
    def __init__(self, kill_value={}):
        self.kill_value = kill_value


class get(character):
    def __init__(self, get_value={}):
        self.get_value = get_value


class checker(character):
    def __init__(self, check_value={}):
        self.check_value = check_value


class c_witch(checker):
    def __init__(self, save=1, kill=1):
        self.save = save
        self.kill = kill


class c_s_wolf(character):
    def __init__(self, kill_value={}, get_value={}):
        self.kill_value = kill_value
        self.get_value = get_value


wolf = killer()
k_wolf = killer()
wk_wolf = killer()
h_wolf = killer()
s_wolf = c_s_wolf()
b_wolf = killer()

wolf = ch("wolf", 0)
k_wolf = ch("k_wolf", 0)
wk_wolf = ch("wk_wolf", 0)
h_wolf = ch("h_wolf", 0)
s_wolf = ch("s_wolf", 0)
b_wolf = ch("b_wolf", 0)

witch = checker()
hunter = checker()
guard = checker()
d_hunter = checker()
knight = checker()

witch = ch("witch", 1)
hunter = ch("hunter", 1)
guard = ch("guard", 1)
d_hunter = ch("d_hunter", 1)
knight = ch("knight", 1)

prophet = get()

prophet = ch("prophet", 1)

cupid = character("cupid", -1)
bomber = character("bomber", 1)
bear = character("bear", 1)
wild_child = character("wild_child", -1)
g_keeper = character("g_keeper", 1)

witch = c_witch()
