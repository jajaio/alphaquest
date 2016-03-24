import random
import colors as c
import classes as cl
import time as t
import anim
import save
import load
import field as f
author="jajaio"


'''
This is a stripped down version of my first game I ever made called "Fight your Foe."
It was a basic number game where you could Attack or Heal against an AI.
I decided to take the old file and turn it into the battle engine for AQ.
'''

def foeattack():
    global player, monster
    print(c.yellow+"Your foe strikes you!")
    t.sleep(1)
    anim.foeattanim()
    player.hp -= monster.att
    player.hp += player.deff

def foeheal():
    global player, monster
    if monster.mp<1:
        print(c.yellow+"Your foe tried to heal, but attacked instead!")
        t.sleep(1)
        anim.foeattanim()
        player.hp -= monster.att
        player.hp += player.deff
    else:
        print(c.yellow+"Your foe heals.")
        t.sleep(1)
        anim.foempanim()
        monster.hp+=30
        monster.mp-=1

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
    global q, player, monster
    if q=="1":
        print(c.yellow+"You attack!")
        t.sleep(1.25)
        anim.playerattanim()
        monster.hp-=player.att
        monster.hp+=monster.deff
    elif q=="2" and player.mp <1:
        print(c.yellow+"You can not heal, so you attack instead.")
        t.sleep(1)
        anim.playerattanim()
        monster.hp-=player.att
        monster.hp+=monster.deff
    elif q=="2":
        print(c.yellow+"You decide to stay back and heal.")
        t.sleep(1)
        anim.playermpanim()
        player.hp+=30
        player.mp-=1

def scanner():
    if player.hp < 1:
        print("You Died!")
        t.sleep(1)
        ter=input(c.yellow+"Do you want to keep playing, or quit? (1), (2)"+c.reset+" >>>"+c.violet).strip()
        if ter == '1':
            f.field()
        elif ter == '2':
            exit()
        else:
            f.field()
    elif monster.hp < 1:
        print(c.yellow+"You won!")
        t.sleep(1)
        curr=random.randint(10,25)
        print("You got "+str(curr)+" Gold!")
        cl.Player.gold+=int(curr)
        t.sleep(1)
        save.save_game()
        input('[Game Saved! Press enter to continue.]')
        f.field()

def fight():
    global q, player, monster
    load.load_game()
    player=cl.Player()
    monster=cl.Foe()
    while True:
        if player.hp < 1:                                                                                                                                                                            
            print("You Died!")                                                                                                                                                                       
            t.sleep(1)                                                                                                                                                                               
            ter=input("Do you want to keep playing, or quit? (1), (2)")                                                                                                                              
            if ter == '1':                                                                                                                                                                           
                break                                                                                                                                                                                
            elif ter == '2':                                                                                                                                                                         
                exit()                                                                                                                                                                               
            else:                                                                                                                                                                                    
                break                                                                                                                                                                                
        elif monster.hp < 1:                                                                                                                                                                         
            print(c.yellow+"You won!")                                                                                                                                                               
            t.sleep(1)                                                                                                                                                                               
            curr=random.randint(10,25)                                                                                                                                                               
            print("You got "+str(curr)+" Gold!")                                                                                                                                                     
            cl.Player.gold+=int(curr)                                                                                                                                                                
            t.sleep(1)                                                                                                                                                                               
            save.save_game()                                                                                                                                                                         
            input('[Game Saved! Press enter to continue.]')                                                                                                                                          
            break     
        else:
            print(c.clear)
            print(c.blue+player.name+str(" HP = ")+str(player.hp)+str(": ")+player.name+str(" MP = ")+str(player.mp))
            print(c.red+monster.mname+str(" HP = "+str(monster.hp)+str(": ")+monster.mname+str(" MP = ")+str(monster.mp)))
            q=input(c.reset+"Attack(1) or Heal(2)? >>>"+c.violet).strip().lower()
            if player.agi >= monster.agi:
                pmove()
                scanner()
                ai()
            elif monster.agi > player.agi:
                ai()
                scanner()
                pmove()

if __name__=='__main__':
    cl.Player=cl.Lost
    cl.Foe=cl.Slime
    fight()
