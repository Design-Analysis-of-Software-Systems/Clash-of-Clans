import unittest
from king import King
import village
import points as pt
class TestKing(unittest.TestCase):
    def testUp(self):
        for n in range(3):
            i=0
            self.Village = village.createVillage(n+1)
            self.Vmap = self.Village.map
            self.d = [0,0]
            self.d[0] = self.Village.dimensions[0]
            self.d[1] = self.Village.dimensions[1]
            p=0
            while(i< self.d[0]):
                j=0
                while(j<self.d[1]):
                    if(self.Vmap[i][j] == pt.BLANK or self.Vmap[i][j] == pt.SPAWN):
                        self.king = King([i,j])
                        # killed before spawning i.e. dead body released
                        if(p==0):
                            # print("lmao")
                            p=1
                            if(self.king.alive == False):
                                p=0
                                self.king.move('up',self.Village)
                                self.assertEqual(self.king.position,[i,j],"FAILED TESTCASE")
                                self.assertEqual([0,0],pt.HERO_POS,"FAILED TESTCASE POS_UPDATE")
                        elif(p==1):
                        # killed anytime after spawning but was spawned alive
                            # print("lol")
                            p=2
                            if(self.king.alive == False):
                                p=1
                                self.king.move('up',self.Village)
                                self.assertEqual(self.king.position,[i,j],"FAILED TESTCASE")
                                self.assertEqual(-1,pt.HERO_POS,"FAILED TESTCASE POS_UPDATE")
                        elif(p==2):
                            # print("ola!")
                            l=0
                            m=i
                            self.king.move('up',self.Village)
                            for k in range(self.king.speed):
                                if(i-k <= 0):
                                    if(l==1):
                                        self.assertEqual(self.king.position,[m,j],"FAILED TESTCASE MOVE")
                                        self.assertEqual(self.king.position,pt.HERO_POS,"FAILED TESTCASE POS_UPDATE")
                                    else:
                                        l=1
                                        m = 0
                                        self.assertEqual(self.king.position,[m,j],"FAILED TESTCASE MOVE")
                                        self.assertEqual(self.king.position,pt.HERO_POS,"FAILED TESTCASE POS_UPDATE")
                                elif(self.Vmap[i-k-1][j] == pt.BLANK or self.Vmap[i-k-1][j] == pt.SPAWN):
                                    if(l==1):
                                        self.assertEqual(self.king.position,[m,j],"FAILED TESTCASE MOVE")
                                        self.assertEqual(self.king.position,pt.HERO_POS,"FAILED TESTCASE POS_UPDATE")
                                    else:
                                        m = i-k-1
                                        self.assertEqual(self.king.position,pt.HERO_POS,"FAILED TESTCASE POS_UPDATE")
                                elif(self.Vmap[i-k-1][j] != pt.BLANK and self.Vmap[i-k-1][j] != pt.SPAWN):
                                    if(l==1):
                                        self.assertEqual(self.king.position,[m,j],"FAILED TESTCASE MOVE")
                                        self.assertEqual(self.king.position,pt.HERO_POS,"FAILED TESTCASE POS_UPDATE")
                                    else:
                                        l=1
                                        m=i-k
                                        self.assertEqual(self.king.position,[m,j],"FAILED TESTCASE MOVE")
                                        self.assertEqual(self.king.position,pt.HERO_POS,"FAILED TESTCASE POS_UPDATE")
                            self.assertEqual(self.king.position,[m,j],"FAILED TESTCASE MOVE")
                    j+=1
                i+=1
    def testDown(self):
        for n in range(3):
            i=0
            self.Village = village.createVillage(n+1)
            self.Vmap = self.Village.map
            self.d = [0,0]
            self.d[0] = self.Village.dimensions[0]
            self.d[1] = self.Village.dimensions[1] 
            p=0
            while(i< self.d[0]):
                j=0
                while(j<self.d[1]):
                    if(self.Vmap[i][j] == pt.BLANK or self.Vmap[i][j] == pt.SPAWN):
                        self.king = King([i,j])
                        # killed before spawning i.e. dead body released
                        if(p==0):
                            # print("lmao")
                            p=1
                            if(self.king.alive == False):
                                p=0
                                self.king.move('down',self.Village)
                                self.assertEqual(self.king.position,[i,j],"FAILED TESTCASE")
                                self.assertEqual([0,0],pt.HERO_POS,"FAILED TESTCASE POS_UPDATE")
                        # killed anytime after spawning but was spawned alive
                        elif(p==1):
                            # print("lol")
                            p=2
                            if(self.king.alive == False):
                                p=1
                                self.king.move('down',self.Village)
                                self.assertEqual(self.king.position,[i,j],"FAILED TESTCASE")
                                self.assertEqual(-1,pt.HERO_POS,"FAILED TESTCASE POS_UPDATE")
                        elif(p==2):
                            # print("ola!")
                            l=0
                            m=i
                            self.king.move('down',self.Village)
                            for k in range(self.king.speed):
                                if(i+k >= (self.d[0] -1)):
                                    if(l==1):
                                        self.assertEqual(self.king.position,[m,j],"FAILED TESTCASE MOVE")
                                        self.assertEqual(self.king.position,pt.HERO_POS,"FAILED TESTCASE POS_UPDATE")
                                    else:
                                        l=1
                                        m = self.d[0] -1
                                        self.assertEqual(self.king.position,[m,j],"FAILED TESTCASE MOVE")
                                        self.assertEqual(self.king.position,pt.HERO_POS,"FAILED TESTCASE POS_UPDATE")
                                elif(self.Vmap[i+k+1][j] == pt.BLANK or self.Vmap[i+k+1][j] == pt.SPAWN):
                                    if(l==1):
                                        self.assertEqual(self.king.position,[m,j],"FAILED TESTCASE MOVE")
                                        self.assertEqual(self.king.position,pt.HERO_POS,"FAILED TESTCASE POS_UPDATE")
                                    else:
                                        m = i+k+1
                                        self.assertEqual(self.king.position,pt.HERO_POS,"FAILED TESTCASE POS_UPDATE")
                                elif(self.Vmap[i+k+1][j] != pt.BLANK and self.Vmap[i+k+1][j] != pt.SPAWN):
                                    if(l==1):
                                        self.assertEqual(self.king.position,[m,j],"FAILED TESTCASE MOVE")
                                        self.assertEqual(self.king.position,pt.HERO_POS,"FAILED TESTCASE POS_UPDATE")
                                    else:
                                        l=1
                                        m=i+k
                                        self.assertEqual(self.king.position,[m,j],"FAILED TESTCASE MOVE")
                                        self.assertEqual(self.king.position,pt.HERO_POS,"FAILED TESTCASE POS_UPDATE")
                            self.assertEqual(self.king.position,[m,j],"FAILED TESTCASE MOVE")
                    j+=1
                i+=1
    def testLeft(self):
        for n in range(3):
            i=0
            self.Village = village.createVillage(n+1)
            self.Vmap = self.Village.map
            self.d = [0,0]
            self.d[0] = self.Village.dimensions[0]
            self.d[1] = self.Village.dimensions[1] 
            p=0
            while(i< self.d[0]):
                j=0
                while(j<self.d[1]):
                    if(self.Vmap[i][j] == pt.BLANK or self.Vmap[i][j] == pt.SPAWN):
                        self.king = King([i,j])
                        # killed before spawning i.e. dead body released
                        if(p==0):
                            # print("lmao")
                            p=1
                            if(self.king.alive == False):
                                p=0
                                self.king.move('left',self.Village)
                                self.assertEqual(self.king.position,[i,j],"FAILED TESTCASE")
                                self.assertEqual([0,0],pt.HERO_POS,"FAILED TESTCASE POS_UPDATE")
                        # killed anytime after spawning but was spawned alive
                        elif(p==1):
                            # print("lol")
                            p=2
                            if(self.king.alive == False):
                                p=1
                                self.king.move('left',self.Village)
                                self.assertEqual(self.king.position,[i,j],"FAILED TESTCASE")
                                self.assertEqual(-1,pt.HERO_POS,"FAILED TESTCASE POS_UPDATE")
                        elif(p==2):
                            # print("ola!")
                            l=0
                            m=j
                            self.king.move('left',self.Village)
                            for k in range(self.king.speed):
                                if(j-k <= 0):
                                    if(l==1):
                                        self.assertEqual(self.king.position,[i,m],"FAILED TESTCASE MOVE")
                                        self.assertEqual(self.king.position,pt.HERO_POS,"FAILED TESTCASE POS_UPDATE")
                                    else:
                                        l=1
                                        m = 0
                                        self.assertEqual(self.king.position,[i,m],"FAILED TESTCASE MOVE")
                                        self.assertEqual(self.king.position,pt.HERO_POS,"FAILED TESTCASE POS_UPDATE")
                                elif(self.Vmap[i][j-k-1] == pt.BLANK or self.Vmap[i][j-k-1] == pt.SPAWN):
                                    if(l==1):
                                        self.assertEqual(self.king.position,[i,m],"FAILED TESTCASE MOVE")
                                        self.assertEqual(self.king.position,pt.HERO_POS,"FAILED TESTCASE POS_UPDATE")
                                    else:
                                        m = j-k-1
                                        self.assertEqual(self.king.position,pt.HERO_POS,"FAILED TESTCASE POS_UPDATE")
                                elif(self.Vmap[i][j-k-1] != pt.BLANK and self.Vmap[i][j-k-1] != pt.SPAWN):
                                    if(l==1):
                                        self.assertEqual(self.king.position,[i,m],"FAILED TESTCASE MOVE")
                                        self.assertEqual(self.king.position,pt.HERO_POS,"FAILED TESTCASE POS_UPDATE")
                                    else:
                                        l=1
                                        m=j-k
                                        self.assertEqual(self.king.position,[i,m],"FAILED TESTCASE MOVE")
                                        self.assertEqual(self.king.position,pt.HERO_POS,"FAILED TESTCASE POS_UPDATE")
                            self.assertEqual(self.king.position,[i,m],"FAILED TESTCASE MOVE")
                    j+=1
                i+=1
    def testRight(self):
        for n in range(3):
            i=0
            self.Village = village.createVillage(n+1)
            self.Vmap = self.Village.map
            self.d = [0,0]
            self.d[0] = self.Village.dimensions[0]
            self.d[1] = self.Village.dimensions[1]
            p=0
            while(i< self.d[0]):
                j=0
                while(j<self.d[1]):
                    if(self.Vmap[i][j] == pt.BLANK or self.Vmap[i][j] == pt.SPAWN):
                        self.king = King([i,j])
                        # killed before spawning i.e. dead body released
                        if(p==0):
                            # print("lmao")
                            p=1
                            if(self.king.alive == False):
                                p=0
                                self.king.move('right',self.Village)
                                self.assertEqual(self.king.position,[i,j],"FAILED TESTCASE")
                                self.assertEqual([0,0],pt.HERO_POS,"FAILED TESTCASE POS_UPDATE")
                        # killed anytime after spawning but was spawned alive
                        elif(p==1):
                            # print("lol")
                            p=2
                            if(self.king.alive == False):
                                p=1
                                self.king.move('right',self.Village)
                                self.assertEqual(self.king.position,[i,j],"FAILED TESTCASE")
                                self.assertEqual(-1,pt.HERO_POS,"FAILED TESTCASE POS_UPDATE")
                        elif(p==2):
                            # print("ola!")
                            l=0
                            m=j
                            self.king.move('right',self.Village)
                            for k in range(self.king.speed):
                                if(j+k >= self.d[1]-1):
                                    if(l==1):
                                        self.assertEqual(self.king.position,[i,m],"FAILED TESTCASE MOVE")
                                        self.assertEqual(self.king.position,pt.HERO_POS,"FAILED TESTCASE POS_UPDATE")
                                    else:
                                        l=1
                                        m = self.d[1]-1
                                        self.assertEqual(self.king.position,[i,m],"FAILED TESTCASE MOVE")
                                        self.assertEqual(self.king.position,pt.HERO_POS,"FAILED TESTCASE POS_UPDATE")
                                elif(self.Vmap[i][j+k+1] == pt.BLANK or self.Vmap[i][j+k+1] == pt.SPAWN):
                                    if(l==1):
                                        self.assertEqual(self.king.position,[i,m],"FAILED TESTCASE MOVE")
                                        self.assertEqual(self.king.position,pt.HERO_POS,"FAILED TESTCASE POS_UPDATE")
                                    else:
                                        m = j+k+1
                                        self.assertEqual(self.king.position,pt.HERO_POS,"FAILED TESTCASE POS_UPDATE")
                                elif(self.Vmap[i][j+k+1] != pt.BLANK and self.Vmap[i][j+k+1] != pt.SPAWN):
                                    if(l==1):
                                        self.assertEqual(self.king.position,[i,m],"FAILED TESTCASE MOVE")
                                        self.assertEqual(self.king.position,pt.HERO_POS,"FAILED TESTCASE POS_UPDATE")
                                    else:
                                        l=1
                                        m=j+k
                                        self.assertEqual(self.king.position,[i,m],"FAILED TESTCASE MOVE")
                                        self.assertEqual(self.king.position,pt.HERO_POS,"FAILED TESTCASE POS_UPDATE")
                            self.assertEqual(self.king.position,[i,m],"FAILED TESTCASE MOVE")
                    j+=1
                i+=1
# unittest.main()
if __name__ == '__main__':

    # Run the test suite and capture the output using TestResult
    suite = unittest.TestLoader().loadTestsFromTestCase(TestKing)
    result = unittest.TestResult()
    
    suite.run(result)
    f = open("output.txt", 'w')

    # Check if all tests passed and print True or False accordingly
    if result.wasSuccessful():
        f.write("True")
        f.close()
        exit(0)
    else:
        f.write("False")
        f.close()
        exit(1)