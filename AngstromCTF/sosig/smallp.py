#!/usr/bin/python
import binascii
from random import choice

class Cipher:
    BLOCK_SIZE = 16
    ROUNDS = 3
    def __init__(self, key):
        assert(len(key) == self.BLOCK_SIZE*self.ROUNDS)
        self.key = key

    def __block_encrypt(self, block):
        enc = int.from_bytes(block, "big")
        for i in range(self.ROUNDS):
            k = int.from_bytes(self.key[i*self.BLOCK_SIZE:(i+1)*self.BLOCK_SIZE], "big")
            enc &= k
            enc ^= k
        return hex(enc)[2:].rjust(self.BLOCK_SIZE*2, "0")


    def __pad(self, msg):
        if len(msg) % self.BLOCK_SIZE != 0:
            return msg + (bytes([0]) * (self.BLOCK_SIZE - (len(msg) % self.BLOCK_SIZE)))
        else:
            return msg
    
    def encrypt(self, msg):
        m = self.__pad(msg)
        e = ""
        for i in range(0, len(m), self.BLOCK_SIZE):
            e += self.__block_encrypt(m[i:i+self.BLOCK_SIZE])
        return e.encode()

key = ("".join([choice(list("abcdef0123456789")) for a in range(Cipher.BLOCK_SIZE*Cipher.ROUNDS*2)]))
print(len(key))
'''
with open("flag", "rb") as f:
    flag = f.read()
'''
#cipher = Cipher(key)


p = "df867dff4e8c6b803ce71342fee27b2eb37eb5d0a985d1861083d503bd93f8df"
#e = cipher.encrypt(binascii.unhexlify(p))
#print(e)
#c = input()
'''
while True:
    a = input("Would you like to encrypt [1], or try encrypting [2]? ")
    if a == "1":

        p = input("What would you like to encrypt: ")
        try:
            print(cipher.encrypt(binascii.unhexlify(p)).decode())
        except:
            print("Invalid input. ")
    elif a == "2":
        for i in range(10):
            p = "".join([choice(list("abcdef0123456789")) for a in range(64)])
            print("Encrypt this:", p)
            e = cipher.encrypt(binascii.unhexlify(p)).decode()
            c = input()
            if e != c:
                print("L")
                exit()
        print("W")
        print(flag.decode())            

    elif a.lower() == "quit":
        print("Bye")
        exit()
    else:
        print("Invalid input. ")
'''
