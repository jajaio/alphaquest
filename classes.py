import colors as c
author="jajaio"

'''TODO
Make advanced player classes
More monsters?
'''
#Yeah, each class should have its own file. But this late in development, I'd rather not spend an hour tweaking all of the code.

class Thing():
	hp=None #Health
	agi=None #Agility
	deff=None #Defense
	att=None #Attack
	mp=None #Magic Power (Ammount of times you can heal)

class Player(Thing):
    gold=0
    name=None

class Foe(Thing):
    mname="Test mob name"
#Advanced Classes
class Assassin(Player):
    hp=75
    agi=70
    deff=7
    att=35
    mp=2
class Paladin(Player):
    hp=100
    agi=55
    deff=10
    att=45
    mp=1
class Wizard(Player):
    hp=75
    agi=70
    deff=5
    att=30
    mp=8
#Basic Classes
class Rogue(Player):
    hp=50
    agi=70
    deff=3
    att=20
    mp=1
class Sellsword(Player):
    hp=65
    agi=45
    deff=5
    att=30
    mp=0
class Cleric(Player):
    hp=40
    agi=65
    deff=3
    att=25
    mp=4
#Lost is the default class, gotta make the player something!
class Lost(Player):
    hp=55
    agi=20
    deff=2
    att=10
    mp=1

#Basic Monster Classes.
class Slime(Foe):
    mname="Slime"
    hp=20
    agi=15
    att=10
    deff=0
    mp=0

class Bandit(Foe):
    mname="Bandit"
    hp=60
    agi=40
    att=20
    deff=2
    mp=1
class Zombie(Foe):
    mname="Zombie"
    hp=55
    agi=10
    att=15
    deff=1
    mp=0
class Skeleton(Foe):
    mname="Skeleton"
    hp=40
    agi=50
    att=25
    deff=2
    mp=1
class Goblin(Foe):
    mname="Goblin"
    hp=75
    agi=20
    att=15
    mp=0
    deff=1
#The dragon, AKA the final boss.
class Dragon(Foe):
    mname="Dragon"
    hp=200
    agi=0
    att=25
    mp=0
    deff=0

def show_cleric():
    tebt='''
    Cleric Stats:
    Health: {c.hp}
    Agility: {c.agi}
    Attack: {c.att}
    Defense: {c.deff}	
    Magic: {c.mp}
    '''
    print(tebt.format(c=Cleric()))
def show_rogue():
    text='''
    Rogue Stats:
    Health: {r.hp}
    Agility: {r.agi}
    Attack: {r.att}
    Defense: {r.deff}
    Magic: {r.mp}
	'''
    print(text.format(r=Rogue()))

def show_sellsword():
    tezt='''
    Sellsword Stats:
    Health: {s.hp}
    Agility: {s.agi}
    Attack: {s.att}
    Defense: {s.deff}
    Magic: {s.mp}
    '''
    print(tezt.format(s=Sellsword()))

def show_assassin():
    assassintext='''
    Assassin Stats:
    Health: {a.hp}
    Agility: {a.agi}
    Attack: {a.att}
    Defense: {a.deff}
    Magic: {a.mp}
    '''
    print(assassintext.format(a=Assassin()))

def show_wizard():
    wizardtext='''
    Wizard Stats:
    Health: {w.hp}
    Agility: {w.agi}
    Attack: {w.att}
    Defense: {w.deff}
    Magic: {w.mp}
    '''
    print(wizardtext.format(w=Wizard()))

def show_paladin():
    paladintext='''
    Paladin Stats:
    Health: {v.hp}
    Agility: {v.agi}
    Attack: {v.att}
    Defense: {v.deff}
    Magic: {v.mp}
    '''
    print(paladintext.format(v=Paladin()))

def show_player():
    yext='''
    {p.name} Stats:
    Health: {p.hp}
    Agility: {p.agi}
    Attack: {p.agi}
    Defense: {p.deff}
    Magic: {p.mp}
    Gold: {p.gold}
    '''
    print(yext.format(p=Player()))

if __name__=='__main__':
    show_rogue()
    show_sellsword()
    show_cleric()
    show_assassin()
    show_wizard()
    show_paladin()
    show_player()
