rom Vessels import vessel
class Champ_Bataille:
    def __init__(self, other, vessel):
        super().__init__(vessel)
        l = 100 # Largeur du champ
        L = 100 # Longueur du champ
        self.cases = [[[0 for x in range(l)] for x in range(L)] for x in [-1,0,1] ] # (x,y,z)=self.cases[x][y][z]
        other.cases = [[[0 for x in range(l)] for x in range(L)] for x in [-1,0,1] ]
        #self.cases et other.cases est une partition du champ de batail selon les vaisseaux de chaque joueurs

    def add_vessel(vessel,self, other,x,y,z):
        self.position=self.cases[x][y][z]
        max_hits = vessel.getmax_hits(self) + vessel.getmax_hits(other)
        if self.position==0 and other.position==0 and sum(max_hits)<= 22 :
            self.position==1
            vessel.coordinates=(x,y,z)
        else:
            print('impossible to add vessel')

    def recevoir_coup(self, other, x, y, z):
        if other.cases[x][y][z] == self.cases[x][y][z] == 0:
            return False
        else :
            return True