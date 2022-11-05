import unittest
from Vessels import vessel
#Vessel nom du fichier, vessel nom de la classe
class vessel(unittest.TestCase):
    def test_go_to(self,x,y,z):
        self.assertEqual(vessel.getcoordinates(self,x,y,z), (x,y,z))
if __name__ == '__main__':
    unittest.main()