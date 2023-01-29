import os
try:
	import wget
except ImportError:
	os.system("pip install wget")
try:
	from dragonxxdlib import *
except ImportError:
	os.system("pip install dragonxxdlib==0.6.2")

inp1=input(" Enter a url : ")

url=(youtube(inp1))

filename = wget.download(url)
