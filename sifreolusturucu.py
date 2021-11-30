#modüller
import random
import time
import sys
import os
from datetime import datetime
import datetime
  
#banner
banner = """
-------------------
SIFRE OLUSTURUCU
Coded by Xale ~ xaletr
-------------------
"""
os.system("clear")
print(banner)

if sys.argv[1] in ["-mg", "--massgenerate"]:
 print("Oluşum 5 Saniye Sonra Başlayacak.")
 print("Çıkış : CTRL + C")
 #######
 dt = datetime.datetime.now()
 ay = dt.month
 yil = dt.year
 gun = dt.day
 date = gun,ay,yil
 print("Tarih : ")
 print(date)
 time.sleep(5)
#olusturma
 a = 1
 while a == 1:
  rndm = random.randint(0,10000000)
  print(rndm)
  
 ########
 
elif sys.argv[1] in ["-g", "--generate"]:
  os.system("clear")
  rndm2 = str(random.randint(0,100000000))
  print("Oluşturulan Şifre : ")
  print(rndm2)
  #######
  dt = datetime.datetime.now()
  ay = dt.month
  yil = dt.year
  gun = dt.day
  date = gun,ay,yil
  
  #######
  print("Şifre Şu Dizine generatepass.txt Olarak Kaydedildi : ")
  dizin = os.system("pwd")
  file = open("generatepass.txt", "w")
  file.write(rndm2)
  print("Tarih : ")
  print(date)
  
elif sys.argv[1] in ["-h", "--help"]:
 print("-------------------------")
 print("YARDIM MENÜSÜ")
 print("-g ~ --generate : Şifre Oluşturur")
 print("-mg ~ --massgenerate : Otomatik Bir Sürü Şifre Oluşturur")
 print("-------------------------")
