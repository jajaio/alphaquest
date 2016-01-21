import classes as cl
import save
import time as t
import colors as c
import field as f
author='jajaio'

'''TODO
Add in save option
Continue working on the shop
'''
def inn():
    innq=input("Welcome to the inn. Would you like to rest here? Or leave? (1), (2)")
    if innq=="1":
        print("You shut your eyes and rest for a bit.")
        t.sleep(.5)
        print("(SAVING GAME...")
        save.save_game()
        print("ogre")
    elif innq=="2":
        pass
    else:
        pass
def hub():
    print(c.clear)
    print(c.yellow+"Welcome to the Pines!")
    hubquestion=input("Would you like to go to the field, shop, or the inn? (1), (2), (3)"+c.reset+" >>>"+c.violet)
    if hubquestion=="1":
        print(c.yellow+"You decide to go to the field.")
        f.field()
    elif hubquestion=="2":
        print(c.yellow+"You decide to go to the shop.")
        t.sleep(1.3)
        shop()
    elif hubquestion=="3":
        inn()

def shop():
    print(c.clear)
    while True:
        question=input("Welcome to the shop! Would you like to see the basic classes or the advanced classes, or leave? (1),(2),(3)").strip()
        if question=="1":
            question_one=input("Okay, would you like to see the the Rogue, Cleric, or Sellsword? (1),(2),(3)").strip()
            if question_one=="1":
                cl.show_rogue()
                buyr=input("Would you like to purchase the Rogue class for 100 Gold? (Y/N)").strip().lower()
                if buyr=="y":
                    if int(cl.Player.gold) >= 100:
                        cl.Player=cl.Rogue
                        print("You are now the Rogue Class!")
                        print(cl.show_player)
                    if int(cl.Player.gold) < 100:
                        print("You need more money! You currently have "+str(cl.Player.gold)+" and you need 100!")
                elif buyr=="n":
                    print("Oh okay.") 
                    shop()
            elif question_one=="2":
                cl.show_cleric()

            elif question_one=="3":
                cl.show_sellsword()
        elif question=="2":
	        #Add in advanced options once made
            pass
        elif question=="3":
            hub()
        else:
            print("I'm not sure if I understand....")
            shop()

if __name__=='__main__':
    hub()
