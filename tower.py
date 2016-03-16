import dragonbattle as db
import town
import time as t
import colors as c
import classes as cl
import save
import load
author='jajaio'

def tower():
    while True:
        print(c.clear)
        print(c.yellow+"You enter a dark tower.")
        t.sleep(1)
        q = input("Would you like to light a torch? Or head back to the town. (1),(2)"+c.reset+" >>>"+c.violet).strip()
        if q == "1":
            print(c.yellow+"You light a torch...")
            t.sleep(1)
            print("A wild Dragon appears!")
            cl.Foe=cl.Dragon
            t.sleep(1)
            db.fight()
        elif q == "2":
            print(c.yellow+"You return to the town.")
            t.sleep(1)
            town.hub()
        else:
            print("I don't know what that means...")
            t.sleep(1)
if __name__=='__main__':
    tower()
