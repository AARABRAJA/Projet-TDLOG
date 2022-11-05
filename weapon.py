##class Weapon:
    ##def __init__(self,ammunitions : int, Range :int ):
      ##  self.ammunitions= ammunition
      ##  self.rannge=rannge

##class lancemissiles_antisurface(Weapon):
  #  def __init__(self, type, coordonnée_x, coordonée_y,coordonnée_z, rayon d action, ammunitions ):
     #   self.type= Surface
    #    self.coordonnée_x=""
      #  self.coordonnée_y=""
       # self.coordonée_z="0"
       # self.rayon d action="30"
       # self.ammuniations="40"

#class lancemissile_anti-air(Weapon):
 #   def _init_(self, type, coordonnée_x, coordonée_y,coordonnée_z, rayon d action, ammunitions ):
  #      self.type= Air
   #     self.coordonnée_x=""
    #    self.coordonnée_y=""
     #   self.coordonée_z>"0"
    #    self.rayon d action="40"
     #   self.ammuniations="50"

#class lance_torpilles(Weapon):
 #   def_init_(self, type, coordonnée_x, coordonée_y,coordonnée_z, rayon action, ammunitions ):
  #      self.type= Sous-marine
   #     self.coordonnée_x=""
     #   self.coordonnée_y=""
    #    self.coordonée_z<"0"
      #  self.rayon d action="20"
       # self.ammuniations="15"

##def fire_at(x,y,z):
  ##  if ammunitions==0:
    ##    return "NOAmmunitionError"
    #if Weapon=lancemissiles_antisurface:
     #   z=0
    #else : return "OutOfRangeError"
    #if Weapon=lancemissile_anti-air:
     # z>0
    #else:
     #   return "OutOfRangeError"
    #if Weapon=lance_torpilles:
     #   z<0
    #else:
     #   return "OutOfRangeError"


class weapon:

    def init(self, ammunitions, Range):
        self.ammunitions = ammunitions
        self.Range = Range

    def fire_at(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

        u = "Lance-missiles antisurface"
        # u= fire_at(x, y, z==0)
        u.type = "surface"
        u.ammunitions = 40
        u.Range = 30
        if z != 0:
            u.ammunitions = u.ammunitions - 1
            print("OutOfRangeError")

        v = "Lance-missiles antiair"
        # v= fire_at(x,y,z>0)
        v.type = "Air"
        v.ammunitions = 50
        v.Range = 40
        if z < 0 or z == 0:
            v.ammunitions = v.ammunitions - 1
            print("OutOfRangeError")

        w = "Lance-torpilles"
        #  w= fire_at(x,y,z<0 or z==0)
        w.tipe = "Sous-marine"
        w.ammunitions = 15
        w.Range = 20
        if z > 0:
            w.ammunitions = w.ammunitions - 1
            print("OutOfRangeError")
        if u.ammunitions or v.ammunitions or w.ammunitions == 0:
            print("NoAmmunitionError")