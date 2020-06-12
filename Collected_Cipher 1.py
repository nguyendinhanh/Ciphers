# -*- coding: latin-1 -*-
#[[x for x in range(1,26) if ((a*x)%26) == 1] for a in range(1,26)]
"""
Created on Wed Jan 15 14:04:31 2020

@authors: Ian Bowler, Connor DiLeo, Megan Marchetti
"""
import sys,os,struct
def chunkstring(string, length=8):
    return (string[i:length+i] for i in range(0, len(string), length))
def padbytes(string,length=8):
	while len(string) < length:
		string += "\x00"
	return string
def encrypt(text,keyphrase,key):
	partial = encrypt1(text,keyphrase)
	return encrypt2(partial,key)
def encrypt1(text,keyphrase):
	tl = len(text)
	kl = len(keyphrase)
	newstr = ""
	for x in range(tl):
		newstr += chr((ord(text[x])+ord(keyphrase[(x%kl)]))%256)
	return newstr
def encrypt2(text,key):
	newstr = ""
	for chunk in chunkstring(text,4):
		chunk = padbytes(chunk,4)
		up =struct.unpack('>L',bytes(chunk,'latin1'))[0]
		p = padbytes(struct.pack('>Q',up*key))
		newstr += p.decode('latin1')
	return newstr
def decrypt(cipher,keyphrase,key):
	partial = decrypt1(cipher,key)
	return decrypt2(partial,keyphrase)
def decrypt1(cipher,key):
	newstr = ""
	for chunk in chunkstring(cipher):
		up =struct.unpack('>Q',bytes(chunk,'latin1'))[0]
		p = struct.pack('>L',up//key)
		newstr += p.decode('latin1')
	newstr = bytes(newstr,'latin1').rstrip(b'\x00').decode('latin1')
	return newstr
def decrypt2(cipher,keyphrase):
	tl = len(cipher)
	kl = len(keyphrase)
	newstr = ""
	for x in range(tl):
		newstr += chr((ord(cipher[x])-ord(keyphrase[(x%kl)]))%256)
	return newstr
def toHex(string):
	newstr=""
	for char in string:
		newstr += hex(ord(char))[2:]
	return newstr
def fromHex(string):
	newstr=""
	for x in range(0,len(string),2):
		newstr+=chr(int(string[x:x+2],16))
	return newstr

#sys.stdout = 1
#sys.stdout = open('filetest.txt', 'w')
def main():
	infloc = sys.argv[2]
	keyphrase = open("cipher.key",'r').read()
	key = int(open("cipher.keycode",'r').read())
	if(sys.argv[1] == 'e'):
		inf = open(infloc,"br")
		instr = inf.read().decode('latin1')
		#print(instr,len(instr))
		outstr = encrypt(instr,keyphrase,key)
	elif(sys.argv[1] == 'd'):
		inf = open(infloc,"br")
		instr = inf.read().decode('latin1')
		#print(instr,len(instr))
		outstr = decrypt(instr,keyphrase,key)
	outf = open(infloc+"_res","bw")
	outf.write(bytes(outstr,"latin1"))
	inf.close()
	outf.close()
	print("done")


if __name__ == '__main__':
	main()
	keyphrase = open("cipher.key",'r').read()
	key =int(open("cipher.keycode",'r').read())
#	print(fromHex("656667"))
#	print(encrypt("getiyt",keyphrase,keycode))
#	print(decrypt("Ã_gyX?x\rÃ§l",keyphrase,keycode))
#	print(decrypt("Ã8hqGuÂ¯",keyphrase,keycode))
