import classes as cl
import save
author='jajaio'

'''TODO
Add in save option
Continue working on the shop
'''
def hub():
	print("Welcome to the Pines!")


def shop():
    while True:
        question=input("Welcome to the Shop! Would you like to see the basic classes or the advanced classes, or leave? (1),(2),(3)").strip()
        if question=="1":
            question_one=input("Okay, would you like to see the the Rouge, Cleric, or Sellsword? (1),(2),(3)").strip()
            if question_one=="1":
                cl.show_rouge()
                buyr=input("Would you like to purchase the Rouge class for 100 Gold? (y/n)").strip().lower()
                if buyr=="y":
                    if int(cl.Player.gold) >= 100:
                        cl.Player=cl.Rouge
                        print("You are now the Rouge Class!")
                        print(cl.Player.hp)
                    if int(cl.Player.gold) < 100:
                        print("You need more money! You currently have "+str(cl.Player.gold)+" and you need 100!")
                elif buyr=="n":
                    print("Oh okay.") 
                    continue
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
	shop()
