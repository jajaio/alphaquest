author="jajaio"
import json
import classes as cl
#Work in progress. May not make it into final release.
def save():
	with open('player.json', 'w') as pfile:
		pfile.write(json.dumps({
            "hp":cl.Player.hp,
            "agi":cl.Player.agi,
            "deff":cl.Player.deff,
            "att":cl.Player.att,
            "mp":cl.Player.mp
            }))
        
if __name__=='__main__':
    save()
