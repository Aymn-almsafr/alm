import os
R="\033[1;31m"
G="\033[1;32m"


print(G,"\n\n\tDownload from Facebook YouTube tiktok\n")
try:
	import wget
except ImportError:
	os.system("pip install wget")
try:
	from dragonxxdlib import *
except ImportError:
	os.system("pip install dragonxxdlib==0.6.2")

inp1=input("\t\t\tEnter a url : ")

url=(youtube(inp1))

filename = wget.download(url)
