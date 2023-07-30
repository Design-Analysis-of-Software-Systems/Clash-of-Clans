import unittest
from king import King
import village
import points
from buildings import Cannon
class TestBonus(unittest.TestCase):
    def setUp(self):
        self.king = King([0, 0])
        self.village = village.createVillage(1)
        self.vmap = self.village.map
        self.cannon = self.village.cannon_objs[points.config['cannons'][0]]
    def testDestroy(self):
        # i.e. if damage given by king > the maximum health of cannon then it should be destroyed
        self.king.attack = self.cannon.max_health + 69
        self.king.attack_target(self.cannon, self.king.attack)
        self.assertTrue(self.cannon.destroy,"TEST FAILED")
    def testAttack(self):
        curr_health = self.cannon.health
        # i.e. damage given by king = damage taken by cannon
        self.king.attack_target(self.cannon, self.king.attack)
        self.assertEqual(self.cannon.health, curr_health - self.king.attack, "TEST FAILED")    
    def testDead(self):
        self.king.alive = False
        curr_health = self.cannon.health
        # i.e. if king is dead no damge should be dealt
        self.king.attack_target(self.cannon, self.king.attack)
        self.assertEqual(self.cannon.health, curr_health, "TEST FAILED")    
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBonus)
    result = unittest.TestResult()    
    suite.run(result)
    f = open("output_bonus.txt", 'w')
    if result.wasSuccessful():
        f.write("True")
        f.close()
        exit(0)
    else:
        f.write("False")
        f.close()
        exit(1)