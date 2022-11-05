
class champ_de_bataille:
    def _init_(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.position = [[0 for x in range(100)] for x in range(100)]


        def positionvalide(x,y,z):
            self.position = self.cases[x][y][z]
            max_hits = getmax_hits(self) + getmax_hits(other)
            if self.position == 0 and self.position == 0 and sum(max_hits) <= 22:
                self.position == 1
                return go_to(x,y,z)
            else:
                print('impossible to add vessel')
