#! /usr/bin/env python3

"""identity2john.py convert asp.Net identity password hashes to john crackable"""

import os
import sys
import binascii
import base64

def process_file(filename):
	try:
		f = open(filename, "rb")
	except (IOError):
		e = sys.exc_info()[1]
		sys.stderr.write("%s : %s\n" % (filename, str(e)))
		return 2
	
	while True:
		line = f.readline()
		if not line:
			break
		process_hash(line.decode().strip())
		
	f.close()
def john_base64_encode(data):
	base64str = base64.b64encode(data).decode()
	
	return base64str.replace('+', '.').strip('=')
	
def process_hash_v2(bin):
	if len(bin) != 49:
		return 0

	salt = bin[1:17]
	hash = bin[17:49]
	return "$%s$%i.%s.%s" % ('pbkdf2-hmac-sha1', 1000, salt.hex(), hash.hex())

def process_hash_v3(bin):
	if len(bin) != 61:
		return 0

	enc = bin[1:5]
	iterations = bin[5:9]
	salt = bin[13:29]
	hash = bin[29:61]
	
	if enc == b'\x00\x00\x00\x00':
		return "$pbkdf2-hmac-sha1$%i.%s.%s" % (int.from_bytes(iterations), salt.hex(), hash.hex())
	elif enc == b'\x00\x00\x00\x01':
		return "$pbkdf2-sha256$%i$%s$%s" % (int.from_bytes(iterations), john_base64_encode(salt), john_base64_encode(hash))
	elif enc == b'\x00\x00\x00\x02':
		return "$pbkdf2-hmac-sha512$%i.%s.%s"% (int.from_bytes(iterations), salt.hex(), hash.hex())
	else:
		return 0
		

def process_hash(hash):
	id = hash.find(':')
	if id > -1 :
		user = hash[0:id]
		bin = base64.b64decode(hash[id+1::])
	else:
		user = 0
		bin = base64.b64decode(hash)
	
	if bin[0] == 0x00 :
		result = process_hash_v2(bin)
	elif bin[0] == 0x01 :
		result = process_hash_v3(bin)
	else:
		result = 0
		
	if not result:
		sys.stderr.write("%s : invalid hash\n" % hash)

	elif user:
		sys.stdout.write("%s:%s\n" % (user, result))
	else:
		sys.stdout.write("%s\n" % result)

if __name__ == "__main__":
	if len(sys.argv) < 2:
		sys.stderr.write("Usage: %s <file>\n" % sys.argv[0])
		sys.exit(1)

	process_file(sys.argv[1])
