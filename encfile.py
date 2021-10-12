import os, sys
import codecs, base64, marshal, zlib
m = "\033[91m"
p = "\033[97m"
h = "\033[90m"
def clear():
	try:
		os.system("clear")
	except OSError:
		os.system("cls")
def banner():
	clear()
	print (f"""{m}
   ________)
  (, /     ,  /)          /)
    /___,    //  _ __   _(/ _  __      __  _/_
 ) /     _(_(/__(/_/ (_(_(_(__/ (_(_/_ /_)_(__
(_/                              .-/.-/
                                (_/(_/
{p}Author	: Pamekasancode
""")
banner()
def help():
	clear()
	print (f"""
{m}Command{p}
------------------------
clear	: membersihkan command line
banner	: menampilkan banner
exit	: keluar

{m}Cara menggunakan?{p}
------------------------------------
endcryption pathfile.py
example	: base64 /sdcard/file.py
Endcryption yang tersedia:
- base64
- base32
- base16
- marshal
- zlib
- hexa
- rot-13
- uu-codec
- cp424
- cp500
- cp875
- cp1026
- cp1252
- bz2codec
- utf-8
- utf-16
- utf-32
file akan tersimpan dengan nama:
encnamafile.py
""")
def filendcrypt():
	while True:
		fenc = input(f"{m}filencrypt {p}> ")
		if "base64" in fenc:
			file = open(fenc.split()[-1], "rb").read()
			enc = base64.b64encode(file)
			fw = open("enc"+fenc.split()[-1], "w")
			fw.write('import base64\nexec(base64.b64decode('+repr(enc.decode("utf-8"))+'))\n')
			fw.close()
		elif "base32" in fenc:
			file = open(fenc.split()[-1], "rb").read()
			enc = base64.b32encode(file)
			fw = open("enc"+fenc.split()[-1], "w")
			fw.write('import base64\nexec(base64.b32decode('+repr(enc.decode("utf-8"))+'))\n')
			fw.close()
		elif "base16" in fenc:
			file = open(fenc.split()[-1], "rb").read()
			enc = base64.b16encode(file)
			fw = open("enc"+fenc.split()[-1], "w")
			fw.write('import base64\nexec(base64.b16decode('+repr(enc.decode("utf-8"))+'))\n')
			fw.close()
		elif "marshal" in fenc:
			file = open(fenc.split()[-1], "r").read()
			co = compile(file, '', 'exec')
			enc = marshal.dumps(co)
			fw = open("enc"+fenc.split()[-1], "w")
			fw.write('import marshal\nexec(marshal.loads('+repr(enc)+'))\n')
			fw.close()
		elif "zlib" in fenc:
			file = open(fenc.split()[-1], "rb").read()
			enc = zlib.compress(file, 9)
			fw = open("enc"+fenc.split()[-1], "w")
			fw.write('import zlib\nexec(zlib.decompress('+repr(enc)+'))\n')
			fw.close()
		elif "hexa" in fenc:
			file = open(fenc.split()[-1], "r").read()
			enc = file.encode().hex()
			fw = open("enc"+fenc.split()[-1], "w")
			fw.write('exec(bytes.fromhex('+repr(enc)+').decode())\n')
			fw.close()
		elif "rot-13" in fenc:
			file = open(fenc.split()[-1], "r").read()
			enc = codecs.encode(file, 'rot-13')
			fw = open("enc"+fenc.split()[-1], "w")
			fw.write('import codecs\nexec(codecs.decode('+repr(enc)+', "rot-13"))\n')
			fw.close()
		elif "uu-codec" in fenc:
			file = open(fenc.split()[-1], "rb").read()
			enc = codecs.encode(file, 'uu-codec')
			fw = open("enc"+fenc.split()[-1], "w")
			fw.write('import codecs\nexec(codecs.decode('+repr(enc)+', "uu-codec"))\n')
			fw.close()
		elif "cp500" in fenc:
			file = open(fenc.split()[-1], "r").read()
			enc = codecs.encode(file, "cp500")
			fw = open("enc"+fenc.split()[-1], "w")
			fw.write('import codecs\nexec(codecs.decode('+repr(enc)+', "cp500"))\n')
			fw.close()
		elif "cp875" in fenc:
                        file = open(fenc.split()[-1], "r").read()
                        enc = codecs.encode(file, "cp875")
                        fw = open("enc"+fenc.split()[-1], "w")
                        fw.write('import codecs\nexec(codecs.decode('+repr(enc)+', "cp875"))\n')
                        fw.close()
		elif "cp1026" in fenc:
                        file = open(fenc.split()[-1], "r").read()
                        enc = codecs.encode(file, "cp1026")
                        fw = open("enc"+fenc.split()[-1], "w")
                        fw.write('import codecs\nexec(codecs.decode('+repr(enc)+', "cp1026"))\n')
                        fw.close()
		elif "cp424" in fenc:
                        file = open(fenc.split()[-1], "r").read()
                        enc = codecs.encode(file, "cp424")
                        fw = open("enc"+fenc.split()[-1], "w")
                        fw.write('import codecs\nexec(codecs.decode('+repr(enc)+', "cp424"))\n')
                        fw.close()
		elif "cp1252" in fenc:
                        file = open(fenc.split()[-1], "r").read()
                        enc = codecs.encode(file, "cp1252")
                        fw = open("enc"+fenc.split()[-1], "w")
                        fw.write('import codecs\nexec(codecs.decode('+repr(enc)+', "cp1252"))\n')
                        fw.close()
		elif "bz2codec" in fenc:
                        file = open(fenc.split()[-1], "rb").read()
                        enc = codecs.encode(file, "bz2-codec")
                        fw = open("enc"+fenc.split()[-1], "w")
                        fw.write('import codecs\nexec(codecs.decode('+repr(enc)+', "bz2-codec"))\n')
                        fw.close()
		elif "utf-8" in fenc:
                        file = open(fenc.split()[-1], "r").read()
                        enc = codecs.encode(file, "utf-8")
                        fw = open("enc"+fenc.split()[-1], "w")
                        fw.write('import codecs\nexec(codecs.decode('+repr(enc)+', "utf-8"))\n')
                        fw.close()
		elif "utf-16" in fenc:
                        file = open(fenc.split()[-1], "r").read()
                        enc = codecs.encode(file, "utf-16")
                        fw = open("enc"+fenc.split()[-1], "w")
                        fw.write('import codecs\nexec(codecs.decode('+repr(enc)+', "utf-16"))\n')
                        fw.close()
		elif "utf-32" in fenc:
                        file = open(fenc.split()[-1], "r").read()
                        enc = codecs.encode(file, "utf-32")
                        fw = open("enc"+fenc.split()[-1], "w")
                        fw.write('import codecs\nexec(codecs.decode('+repr(enc)+', "utf-32"))\n')
                        fw.close()
		elif fenc == "clear":
			clear()
		elif fenc == "banner":
			banner()
		elif fenc == "help":
			help()
		elif fenc == "exit":
			sys.exit()
		else:
			print (fenc+" tidak ada dalam command")
try:
	filendcrypt()
except KeyboardInterrupt:
	print ("Ctrl + C = keluar")
	sys.exit()
