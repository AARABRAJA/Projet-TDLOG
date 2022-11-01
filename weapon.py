class Weapon:
    def _init_(self,ammunitions int, Range int ):
        self.ammunitions= ammunition
        self.Range=Range

class lancemissiles_antisurface(Weapon):
    def _init_(self, type, coordonnée_x, coordonée_y,coordonnée_z, rayon d action, ammunitions ):
        self.type= Surface
        self.coordonnée_x=""
        self.coordonnée_y=""
        self.coordonée_z="0"
        self.rayon d action="30"
        self.ammuniations="40"

class lancemissile_anti-air(Weapon):
    def _init_(self, type, coordonnée_x, coordonée_y,coordonnée_z, rayon d action, ammunitions ):
        self.type= Air
        self.coordonnée_x=""
        self.coordonnée_y=""
        self.coordonée_z>"0"
        self.rayon d action="40"
        self.ammuniations="50"

class lance_torpilles(Weapon):
    def _init_(self, type, coordonnée_x, coordonée_y,coordonnée_z, rayon d action, ammunitions ):
        self.type= Sous-marine
        self.coordonnée_x=""
        self.coordonnée_y=""
        self.coordonée_z<"0"
        self.rayon d action="20"
        self.ammuniations="15"

def fire_at(x,y,z):
    if ammunitions==0:
        return "NOAmmunitionError"
    if Weapon=lancemissiles_antisurface:
        z=0
    else : return "OutOfRangeError"
    if Weapon=lancemissile_anti-air:
        z>0
    else:
        return "OutOfRangeError"
    if Weapon=lance_torpilles:
        z<0
    else:
        return "OutOfRangeError"