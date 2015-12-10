import classes as cl
import json
def load_game():
    with open('player.json', 'r') as pfile:
        j=json.load(pfile)
        cl.Player.hp=j['hp']
        cl.Player.agi=j['agi']
        cl.Player.deff=j['deff']
        cl.Player.att=j['att']
        cl.Player.mp=j['mp']
        
