import urllib3
from bs4 import BeautifulSoup
import sys

SRC_URL = 'http://www.oxfordlearnersdictionaries.com/definition/english/'
LOOP = 0


inword = input('Enter a word to search: ')
inword = inword.lower()
http = urllib3.PoolManager()

urltofire = SRC_URL  + inword
r = http.request('GET', urltofire)
soup = BeautifulSoup(r.data,"html.parser")

#print(soup.encode("utf-8"))
# old code to fetch single definition and single example
'''
try:
	defn = soup.body.find('span',attrs={'class':'def'}).text
except Exception :
	print("")
	print("=== Error: Word not found in database.")
	print("=== Error is ", sys.exc_info()[0])
	exit()

print("")	
print("=== meaning is :" )
print(defn)


#handles only one meaning and one example presently
try:
	eg = soup.body.find('span',attrs={'class':'x-g'}).text
except Exception :
	print("")
	print("=== No examples found for: " , inword)
	exit()	

print("")	
print("=== examples : ")
print(eg)
'''
def_found = False;
eg_found = False;
extra_found = False;

print("")
print(">>> Trying Source 1...." , end=' ')

alldefns = soup.findAll("span", {"class" : "def"})

#print(alldefns)

try:
	for alldefn in alldefns:
		if LOOP == 0:
			print("[PASS]")		
			print("\n====== Definitions =====")
		LOOP = LOOP + 1
		print("%d. %s" %(LOOP,alldefn.text))
		def_found = True
except Exception:
	pass

	
LOOP = 0

if def_found == False :
#	print("yay: " + urltofire)
	print("[FAILED]")
	urltofire = SRC_URL +inword + '1'
	r = http.request('GET', urltofire)
	soup = BeautifulSoup(r.data,"html.parser")
	alldefns = soup.findAll("span", {"class" : "def"})

	print(">>> Now trying Source 2....", end=' ')	
	
	try:
		for alldefn in alldefns :
			if LOOP == 0:
				print("[PASS]")			
				print("====== Definitions =====")
			LOOP = LOOP + 1
			print("%d. %s" %(LOOP,alldefn.text))
			def_found = True
	except Exception:
		pass

'''
if ~def_found :
	print("yay22: "  + urltofire)		'''
	
if def_found == False: 
	print("[FAILED]")
	print("Sorry, No definitions found for: " + inword)

print("")
print("====== Examples =====")
#results = soup.findAll("span",{"class":"x-g")
allegs = soup.findAll("span", {"class" : "x"})

#soup = soup.encode("utf-8")

LOOP = 0
try:
	for alleg in allegs :
		LOOP = LOOP + 1	
		print("%d. %s" %(LOOP, alleg.text))
		eg_found = True;
except Exception:
	pass

if eg_found == False:
		print("Sorry, No examples found for: " + inword)

'''		
for span in soup.find_all("span", {"class" : "x"}):
	print(" ******hihihihi " ) 
	spanbyte= span.encode("utf-8")
	print(spanbyte)
	'''
try:	
	attr1=soup.body.find('div',attrs={'class':'sound audio_play_button pron-uk icon-audio'}).attrs
	attr2=soup.body.find('div',attrs={'class':'sound audio_play_button pron-us icon-audio'}).attrs
	print("")
	print("=== Extra information =========")
	print("UK pronunciation: " + attr1['data-src-mp3'])
	print("US pronunciation: " + attr2['data-src-mp3'])
	print("===============================")	
except Exception:
	pass



# code works till here...next are new features of the lab
