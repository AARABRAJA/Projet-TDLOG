import unittest
from Weapon.py import weapon

class Weapon(unittest.TestCase):
    def test_fire_at(self,x,y,z):
        self.assertEqual(Weapon.test_fire_at(self,x,y,z), x,y,z)


if _name_ == '_main_':
    unittest.main()