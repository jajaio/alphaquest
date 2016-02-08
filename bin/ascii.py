import time
import colors as c

hero1='''
      |
      |
\_0___+                                                                                                                                                                               
  |                                                                                                                                                                                        
  |                                                                                                                                                                                        
 / /   
'''

hero2='''


\_0___+----
  |
  |
 / /
'''

def attackanime():
    for count in range(2):
        print(hero1)
        time.sleep(.25)
        print(c.clear)
        print(hero2)
        time.sleep(.25)
        print(c.clear)
if __name__=='__main__':
    attackanime()
