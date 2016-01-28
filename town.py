import classes as cl
import save
import time as t
import colors as c
import field as f
author='jajaio'

'''TODO
Continue working on the shop
COLORS!
'''
def inn():
    print(c.clear)
    innq=input(c.yellow+"Welcome to the inn. Would you like to rest here? Or leave? (1), (2)"+c.reset+">>>"+c.violet)
    if innq=="1":
        print(c.yellow+"You shut your eyes and rest for a bit.")
        t.sleep(.5)
        print("[Game saved!]")
        save.save_game()
        print("You wake up feeling rested...")
        t.sleep(1.5)
        hub()
    elif innq=="2":
        hub()
    else:
        print(c.yellow+"I don't understand...")
        inn()

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
        question=input(c.yellow+"Welcome to the shop! Would you like to see our professions? Or would you like to leave? (1), (2)"+c.reset+" >>>"+c.violet).strip()
        if question=="1":
            question_one=input(c.yellow+"Okay, would you like to see the the Rogue, Cleric, or Sellsword? (1),(2),(3)"+c.reset+" >>>"+c.violet).strip()
            if question_one=="1":
                cl.show_rogue()
                buyr=input(c.yellow+"Would you like to purchase the Rogue class for 100 Gold? (Y/N)"+c.reset+" >>>"+c.violet).strip().lower()
                if buyr=="y":
                    if int(cl.Player.gold) >= 100:
                        cl.Player=cl.Rogue
                        print(c.yellow+"You are now a Rogue!")
                        t.sleep(1)
                        print(c.yellow+str(cl.show_player()))
                        print()
                        input("[Press enter to continue]")
                        hub()
                    if int(cl.Player.gold) < 100:
                        print(c.yellow+"You need more money! You currently have "+str(cl.Player.gold)+" and you need 100!")
                        hub()
                elif buyr=="n":
                    print(c.yellow+"Oh, okay.")
                    t.sleep(1)
                    shop()
            elif question_one=="2":
                cl.show_cleric()
                buyd=input(c.yellow+"Would you like to purchase the Cleric class for 100 gold? (Y/N)"+c.reset+" >>>"+c.violet).strip().lower()
                if buyd=="y":
                    if int(cl.Player.gold) >= 100:
                        cl.Player=cl.Cleric
                        print(c.yellow+"You are now a Cleric!")
                        t.sleep(1)
                        print(str(cl.show_player()))
                        print()
                        input("[Press enter to continue]")
                        hub()
                    if int(cl.Player.gold) <= 100:
                        print(c.yellow+"You need more money! You currently have "+str(cl.Player.gold)+" and you need 100!")
                        hub()
            elif question_one=="3":
                cl.show_sellsword()
                buyf=input(c.yellow+"Would you like to purchase the Sellsword class for 100 gold? (Y/N)"+c.reset+" >>>"+c.violet).strip().lower()
                if buyf=="y":
                    if int(cl.Player.gold) >= 100:
                        cl.Player=cl.Cleric
                        print(c.yellow+"You are now a Sellsword!")
                        t.sleep(1)
                        print(cl.show_player())
                        print()
                        input("[Press enter to continue]")
                    if int(cl.Player.gold) <= 100:
                        print(c.yellow+"You need more money! You currently have "+str(cl.Player.gold)+" and you need 100!")
                        hub()
                elif buyf=="n":
                    print(c.yellow+"Oh, okay.")
                    t.sleep(1)
                    shop()
                else:
                    print(c.yellow+"I'm not sure if I understand...")
                    t.sleep(1.25)
                    shop()
        elif question=="2":
            hub()
        else:
            print(c.yellow+"I'm not sure if I understand...")
            t.sleep(1.25)
            shop()
if __name__=='__main__':
    hub()
