import random
import colors as c
import classes as cl

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
	if cl.Foe.heals<1:
		print("Your foe tried to heal, but attacked instead!")
		cl.Player.hp -= 10
	else:
		print("Your foe Heals")
		cl.Foe.hp=cl.Foe.hp+35
		cl.Foe.heals=cl.Foe.heals-1

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
			print("PLAYER HP ="+str(cl.Player.hp)+"PLAYER HEALS ="+str(cl.Player.mp))
			print("FOE HP ="+str(cl.Foe.hp)+"FOE HEALS ="+str(cl.Foe.mp))
			q=input("Attack(1) or Heal(2)? >>>").strip().lower()
			if q=="1":
				print("You attack your foe!")
				cl.Foe.hp=cl.Foe.hp-10
			elif q=="2" and cl.Player.mp<1:
				print("You are out of heals, you attack instead.")
				cl.Foe.hp=cl.Foe.hp-10
			elif q=="2":
				print("You decide to stay back and heal.")
				cl.Player.hp=cl.Player.hp+3
	ai()
if __name__=='__main__':
	fight()
