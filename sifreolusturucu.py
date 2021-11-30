#modüller
import random
import time
import sys

#banner
banner = """
-------------------
SIFRE OLUSTURUCU
Coded by Xale ~ xaletr
-------------------
"""
print(banner)

if sys.argv[1] in ["-mg", "--massgenerate"]:
 print("Oluşum 5 Saniye Sonra Başlayacak.")
 print("Çıkış : CTRL + C")
 time.sleep(5)
#olusturma
 a = 1
 while a == 1:
  rndm = random.randint(0,10000000)
  print(rndm)
elif sys.argv[1] in ["-g", "--generate"]:
  rndm2 = random.randint(0,100000000)
  print("Oluşturulan Şifre : ")
  print(rndm2)
