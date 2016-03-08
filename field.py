author="jajaio"
import battleengine as b
import random
import classes as cl
import colors as c
import time as t
import town
def random_monster():
    monsters=[cl.Slime, cl.Bandit, cl.Zombie, cl.Skeleton, cl.Goblin]
    monster=random.choice(monsters)
    cl.Foe=monster

def field():
    print(c.clear)
    print(c.yellow+"You are in a grassy field.")
    t.sleep(1)
    f=input(c.yellow+"Do you want to look for monsters? Or go back to the town? (1), (2)"+c.reset+" >>>"+c.violet)
    if f=="1":
        print(c.yellow+"You decide to look around.")
        t.sleep(1.5)
        print(c.reset)
        print(c.clear)
        print(".")
        t.sleep(.5)
        print(c.clear)
        print("..")
        t.sleep(.5)
        print(c.clear)
        print("...")
        t.sleep(.5)
        print(c.clear)
        random_monster()
        print(c.yellow+"You found a random "+c.red+cl.Foe.mname+c.yellow+"!")
        t.sleep(1)
        b.fight()
        field()
    elif f=="2":
        print(c.yellow+"You decide to go back to the town...")
        t.sleep(1.25)
        town.hub()
    else:
        print("I don't know what you mean....")
        t.sleep(1)
        field()

if __name__=='__main__':
    cl.Player=cl.Lost
    field()
