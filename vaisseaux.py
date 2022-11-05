rom Weapon import weapon
from Vessels import vessel


u = "Lance-missiles antisurface"
v = "Lance-missiles antiair"
w = "Lance-torpilles"

Cruiser= vessel (weapon=v)
Cruiser.max_hits=6
Cruiser.coordinates=(int,int,0)

Submarine = vessel (weapon=w)
Submarine.max_hits=2
Submarine.coordinates=(int,int,0 or -1)

Fregate = vessel (weapon=u)
Fregate.max_hits=5
Fregate.coordinates=(int,int,0)

Destroyer = vessel (weapon=w)
Destroyer.max_hits=4
Destroyer.coordinates=(int,int,0)

Aircraft = vessel (weapon=u)
Aircraft.max_hits=1
Aircraft.coordinates=(int,int,1)

