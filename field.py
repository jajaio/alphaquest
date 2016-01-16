author="jajaio"
import battleengine as b
import random
import classes as cl
import colors as c
import time as t

def random_monster():
    monsters=[cl.Slime, cl.Bandit, cl.Zombie, cl.Skeleton, cl.Goblin]
    monster=random.choice(monsters)
    cl.Foe=monster

def field():
    print("You are in a grassy field.")
    f=input("Do you want to look for monsters? Or go back to the town? (1), (2)")
    if f=="1":
        print("You decide to look around.")
        t.sleep(1.5)
        print(c.clear)
        print(".")
        t.sleep(.5)
        print(c.clear)
        print("..")
        t.sleep(.5)
        print(c.clear)
        t.sleep(.5)
        print("...")
        t.sleep(.5)
        print(c.clear)
        random_monster()
        print("You found a random "+cl.Foe.mname+"!")
        t.sleep(1)
        b.fight()
        field()
    elif f=="2":
        pass
    else:
        pass

if __name__=='__main__':
    field()
