import os
import sys

red = "\033[1;31;40m"
clear = "\033[1;0;00m"


print red + '''
 _         _         
| |_  __ _(_)___ ___ 
| ' \/ _` | (_-</ -_)
|_||_\__,_|_/__/\___|

''' + clear + '''>> Internal Pentest Framework <<'''

command = 1
print("\n")

while command != "exit":
	command = raw_input("COMMAND"+red+"|>" + clear)

	if command == "":
		command = 1

	elif command == "hosts":
		print("\n")
		os.system('cat hosts.txt')
		print("\n")

	elif command == "alive":
		os.system('nmap -sn -iL hosts.txt')

	elif command == "clear":
		os.system('clear')

	elif command == "ports":
		os.system('python3 nmapScanner.py')

	elif command == "dir":
		os.system("cat hosts.txt | xargs -I{}  python3 dirsearch/dirsearch.py -u http://{} -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt  -e php,jsp,rb,py,js,asp,aspx,zip,sql,tar,txt,key,doc,docx,html,jar,groovy,back,xml,ini,inc,config,json,yml,conf,cgi --plain-text-report=dir/http:{}.txt")

	elif command == "headers":
		os.system("cat hosts.txt | xargs -I{} sh -c 'curl -sI http://{} > headers/{}.txt'")

	elif command == "ids":
		os.system("cat hosts.txt | xargs -I{} sh -c 'lbd {} | grep does'")
		os.system("cat hosts.txt | xargs -I{} sh -c 'wafw00f {} | grep site'")

	elif command == "scan":
		os.system('python3 nmapScanner.py')
		os.system("cat hosts.txt | xargs -I{}  python3 dirsearch/dirsearch.py -u http://{} -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt  -e php,jsp,rb,py,js,asp,aspx,zip,sql,tar,txt,key,doc,docx,html,jar,groovy,back,xml,ini,inc,config,json,yml,conf,cgi --plain-text-report=dir/http:{}.txt")
		os.system("cat hosts.txt | xargs -I{} sh -c 'curl -sI http://{} > headers/{}.txt'")

	elif command == "smb":
		os.system("cat hosts.txt | xargs -I{} sh -c 'crackmapexec smb {}'")


	elif command == "help":

		print '''
		[exit]
		[clear]
		[hosts]	list all hosts
		[alive]	check if hosts are alive
		[ports]	port scan of all hosts
		[dir]	Directory Enumuration
	    [headers]	Grab Web Headers
		[scan]	Port Scan and Directory Enumuration of all hosts 
		[ids] Detect Intrusion Detection System
		[smb] Check for SMB Services


		'''

	else:
		print "[+] Unknown Command"