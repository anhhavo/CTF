"""
DIFFIE HELLMAN ATTACK
Given p,g,A,B--> Obtain a,b
"""

from __future__ import print_function
import math
from discreteLogarithm import *

### a^b mod m
### pow(a,b)%m == pow(a,b,m)

# Variables Used
p = int(input("Enter value for p: ")) #Example: 10784399
g = int(input("Enter value for g: ")) #Example:13
A = int(input("Enter value for A: ")) #Example:10306738
B = int(input("Enter value for B: ")) #Example:1206314

print("\nGiven this values: \n-------------------- \n")
print("p =", str(p) )
print("g =", str(g) )
print("A =", str(A) )
print("B =", str(B) )

print("\nSolving...: \n-------------------- \n")
print("Alice sends to Bob: ")
# Alice Sends Bob A = g^a mod p
a = baby_steps_giant_steps(g,A,p)
print( "a = ", str(a) )

print("\nBob sends to Alice: ")
# Bob Sends Alice B = g^b mod p
b = baby_steps_giant_steps(g,B,p)
print( "b = ", str(b) )

print("\nPrivate Keys: \n-------------------- \n")
# Alice Computes Shared Secret: s = B^a mod p
k_alice = pow(B,a,p)

print( "K (Alice private key): ", str(k_alice))
k_bob = pow(B,b,p)
print( "K (Bob private key): ", str(k_bob))
