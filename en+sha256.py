# encrypt sha256
import hashlib

str=str,',{.c][o^uecnlkijh*.iomv:QzCFRcd;drof/zx}w;ls.e85T^#ASwa?=(lk'

str=hashlib.sha256(str.encode()).hexdigest().upper()


################




""" with open('encrypt4.py','w') as file:
    file.writelines(str(encrypt4)) """
###############
    
file_formate = open('encrypt4.py','r')
fromateto = file_formate.read()
distdormated = fromateto.replace("\r\n", "\n").replace("\t","    ")
print(distdormated.replace("\t","\\t"))
    





#############
