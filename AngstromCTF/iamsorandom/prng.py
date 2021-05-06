

import time
import random
import os

class Generator():
    DIGITS = 8
    def __init__(self, seed):
        self.seed = seed
        assert(len(str(self.seed)) == self.DIGITS)
        print("part1: ", self.seed)
        x1 = str(self.seed**2).rjust(self.DIGITS*2, "0") #[self.DIGITS//2:self.DIGITS + self.DIGITS//2]
        print((x1))
        x2 = str(self.seed**2).rjust(self.DIGITS*2, "0")[4:12]
        print("x2: ",x2)
    def getNum(self):
        #print("part2: ")
        self.seed = int(str(self.seed**2).rjust(self.DIGITS*2, "0")[4:12])
        print("New seed is :", self.seed)
        return self.seed


#r1 = (random.randint(10000000, 99999999))
#r2 = (random.randint(10000000, 99999999))
r1 = 14849670 
r2 = 16315175
r3 = 51269910
r4 = 18493528
print (str(r3**2).rjust(16, "0")[4:12])
print (str(r4**2).rjust(16, "0")[4:12])
print(r1, r2)
d1 = Generator(r1)
d2 = Generator(r2)
d_1 = d1.getNum()
d_2 = d2.getNum()
print("d1 getNum: ",d_1)
print("d2 getNum: ",d_2)
print(d_1*d_2)
print("------------------")
#print(d1.getnum() * d2.getNum())
print(d1.getNum() * d2.getNum())
#print(d1.getNum() * d2.getNum())
print("r1*r2 = ", r1*r2)
print("######################################")
#Trial 
a = 86153853 #928191 #27129491 #96645079
b = 95959616 #82492179 #86370278 #1365175
a_d1 = int((str(a**2).rjust(16, "0")[4:12]))
b_d1 = int(str(b**2).rjust(16, "0")[4:12])
#a_d1 = Generator(a)
#b_d1 = Generator(b)
print("new seed a: ", a_d1)
print("new seed b: ", b_d1)
print(a_d1*b_d1)
query_counter = 0

actf{middle_square_method_more_like_middle_fail_method}
