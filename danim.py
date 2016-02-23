import colors as c
import time as t

dragonatt1='''
         __        _
       _/  \    _(\(o
      /     \  /  _  ^^^o
     /   !   \/  ! '!!!v'
    !  !  \ _' ( \____       
    ! . \ _!\   \===^\) 
     \ \_!  / __!         
      \!   /    \\     
(\_      _/   _\ )        
 \ ^^--^^ __-^ /(__      
  ^^----^^    "^--v'
'''
dragonatt2='''
         __        _
       _/  \    _(\(o       ____
      /     \  /  _  ^^^o  {    }
     /   !   \/  ! '!!!v'  {____}
    !  !  \ _' ( \____       
    ! . \ _!\   \===^\) 
     \ \_!  / __!         
      \!   /    \\     
(\_      _/   _\ )        
 \ ^^--^^ __-^ /(__      
  ^^----^^    "^--v'
'''
dragonatt3='''
         __        _
       _/  \    _(\(o           ____
      /     \  /  _  ^^^o      {    }
     /   !   \/  ! '!!!v'      {____}
    !  !  \ _' ( \____       
    ! . \ _!\   \===^\) 
     \ \_!  / __!         
      \!   /    \\     
(\_      _/   _\ )        
 \ ^^--^^ __-^ /(__      
  ^^----^^    "^--v'
'''
dragonatt4='''
         __        _
       _/  \    _(\(o               ____
      /     \  /  _  ^^^o          {    }
     /   !   \/  ! '!!!v'          {____}
    !  !  \ _' ( \____       
    ! . \ _!\   \===^\) 
     \ \_!  / __!         
      \!   /    \\     
(\_      _/   _\ )        
 \ ^^--^^ __-^ /(__      
  ^^----^^    "^--v'
'''

def dragonattanim():
    print(c.clear)
    print(dragonatt1)
    t.sleep(.3)
    print(c.clear)
    print(dragonatt2)
    t.sleep(.3)
    print(c.clear)
    print(dragonatt3)
    t.sleep(.3)
    print(c.clear)
    print(dragonatt4)
    t.sleep(.3)
if __name__=='__main__':
    dragonattanim()
