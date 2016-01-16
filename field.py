author="jajaio"
import battleengine as b
import random
import classes as cl
def random_monster():
    monsters=[cl.Slime, cl.Bandit, cl.Zombie, cl.Skeleton, cl.Goblin]
    monster=random.choice(monsters)
    cl.Foe=monster
    print(cl.Foe.mname)

def field():
    print("You arive in a grassy field.")

if __name__=='__main__':
    random_monster()
