author="jajaio"
import json
import classes as cl
author="jajaio"
#The player can save their game in the town.

def save_game():
	with open('player.json', 'w') as pfile:
		pfile.write(json.dumps({
            "hp":cl.Player.hp,
            "agi":cl.Player.agi,
            "deff":cl.Player.deff,
            "att":cl.Player.att,
            "mp":cl.Player.mp
            }))
        
if __name__=='__main__':
    save_game()
