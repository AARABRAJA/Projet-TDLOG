from Weapon import weapon
from Vessels import vessel


u = "Lance-missiles antisurface"
v = "Lance-missiles antiair"
w = "Lance-torpilles"

Cruiser= vessel (weapon=v)
vessel.go_to(Cruiser,'x:int','y:int','z=0')
Cruiser.max_hits=6

Submarine = vessel (weapon=w)
vessel.go_to(Submarine,'x:int','y:int','z=0' or 'z=-1')
Submarine.max_hits=2

Fregate = vessel (weapon=u)
vessel.go_to(Fregate,'x:int','y:int','z=0')
Fregate.max_hits=5

Destroyer = vessel (weapon=w)
vessel.go_to(Destroyer,'x:int','y:int','z=0')
Destroyer.max_hits=4

Aircraft = vessel (weapon=u)
vessel.go_to(Aircraft,'x:int','y:int','z=1')
Aircraft.max_hits=1