
import os
import zlib
def keystream():
	key = os.urandom(2)
	index = 0
	while 1:
		index+=1
		if index >= len(key):
			key += zlib.crc32(key).to_bytes(4,'big')
			#print(key)
		yield key[index]
ciphertext = []
with open("plain","rb") as f:
	plain = f.read()

	k = keystream()
	for i in plain:
		j = (next(k))
		#print(j)
		#print(i)
		ciphertext.append(i ^ j)

with open("enc","rb") as g:
	cipher = g.read()
print(cipher)
#for c in cipher:
	#print(cipher)

for i in range(65536):
	msg21 = []
	k = keystream(i.to_bytes(2,byteorder="big"))
	for j in cipher: 
		msg1.append(j ^ next(k))
	msg2 = bytes(msg1)
	if b"actf{" in msg2:
		print(msg2)

