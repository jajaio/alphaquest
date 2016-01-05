import random
import colors as c
import classes as cl
import time as t
author="jajaio"

'''
This is a stripped down version of my first game I ever made called "Fight your Foe."
It was a basic number game where you couldAttack or Heal against an AI.
I decided to take the old file and turn it into the battle engine for AQ.
'''

def select_enemy():
    pass

'''TODO
Change all classes to be <cl.Class.stat>
Take out any old stuff
Fix indents
'''

def foeattack():
	print("Your foe strikes you!")
	cl.Player.hp -= 10
def foeheal():
    if cl.Foe.mp<1:
        print("Your foe tried to heal, but attacked instead!")
        cl.Player.hp -= 10
        t.sleep(4)
    else:
        print("Your foe Heals")
        t.sleep(3)
        cl.Foe.hp=cl.Foe.hp+35
        cl.Foe.mp=cl.Foe.mp-1

def ai():
	listy=[foeheal,foeattack]
	move=random.choice(listy)
	if move==foeheal:
		foeheal()
	elif move==foeattack:
		foeattack()
	else:
		input("Fatal Error")

def fight():
    while True:
        if cl.Player.hp < 1:
            input("You Died!")
            break
        elif cl.Foe.hp < 1:
            input("You won!")
            break
        else:
            print(c.clear)
            print(cl.Player.name+str(" HP = ")+str(cl.Player.hp)+str(": ")+cl.Player.name+str(" HEALS = ")+str(cl.Player.mp))
            print("FOE HP = "+str(cl.Foe.hp)+str(": ")+str(" FOE HEALS = ")+str(cl.Foe.mp))
            q=input("Attack(1) or Heal(2)? >>>").strip().lower()
            if q=="1":
                print("You attack your foe!")
                cl.Foe.hp=cl.Foe.hp-10
            elif q=="2" and cl.Player.mp<1:
                print("You are out of heals, you attack instead.")
                t.sleep(1)
                cl.Foe.hp=cl.Foe.hp-10
            elif q=="2":
                print("You decide to stay back and heal.")
                cl.Player.hp+=10
                cl.Player.mp-=1
    ai()
if __name__=='__main__':
    fight()
