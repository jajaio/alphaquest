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


'''TODO
Done! I think...
'''

def foeattack():
    print(c.yellow+"Your foe strikes you!")
    t.sleep(1)
    cl.Player.hp -= cl.Foe.att
def foeheal():
    if cl.Foe.mp<1:
        print(c.yellow+"Your foe tried to heal, but attacked instead!")
        t.sleep(1)
        cl.Player.hp -= cl.Foe.att
    else:
        print(c.yellow+"Your foe Heals")
        t.sleep(1)
        cl.Foe.hp+=10
        cl.Foe.mp-=1

def ai():
	listy=[foeheal,foeattack]
	move=random.choice(listy)
	if move==foeheal:
		foeheal()
	elif move==foeattack:
		foeattack()
	else:
		input("Fatal Error")

def pmove():
    global q
    if q=="1":
        print(c.yellow+"You attack!")
        t.sleep(1)
        cl.Foe.hp-=cl.Player.att
        cl.Foe.hp+=cl.Foe.deff
    elif q=="2" and cl.Player.mp <1:
        print(c.yellow+"You can not heal, so you attack instead.")
        t.sleep(1)
        cl.Foe.hp-=cl.Player.att
        cl.Foe.hp+=cl.Foe.deff
    elif q=="2":
        print(c.yellow+"You decide to stay back and heal.")
        t.sleep(1)
        cl.Player.hp+=10
        cl.Player.mp-=1

def fight():
    global q
    while True:
        if cl.Player.hp < 1:
            input("You Died!")
            t.sleep(1)
            break
        elif cl.Foe.hp < 1:
            print(c.yellow+"You won!")
            t.sleep(1)
            curr=random.randint(10,25)
            print("You got "+str(curr)+" Gold!")
            cl.Player.gold+=curr
            t.sleep(1)
            break
        else:
            print(c.clear)
            print(c.blue+cl.Player.name+str(" HP = ")+str(cl.Player.hp)+str(": ")+cl.Player.name+str(" MP = ")+str(cl.Player.mp))
            print(c.red+"FOE HP = "+str(cl.Foe.hp)+str(": ")+str(" FOE MP = ")+str(cl.Foe.mp))
            q=input(c.reset+"Attack(1) or Heal(2)? >>>").strip().lower()
            if cl.Player.agi >= cl.Foe.agi:
                pmove()
                ai()
            elif cl.Foe.agi > cl.Player.agi:
                ai()
                pmove()
if __name__=='__main__':
    fight()
