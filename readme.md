# haise
## Internal Network Pentest Framework
![](https://github.com/syedumerqadri/haise/blob/master/image.jpg)


## Internal Penetration Testing:

An Internal Penetration Test differs from a vulnerability assessment in that it actually exploits the vulnerabilities to determine what information is actually exposed. An Internal Penetration Test mimics the actions of an actual attacker exploiting weaknesses in network security without the usual dangers. This test examines internal IT systems for any weakness that could be used to disrupt the confidentiality, availability or integrity of the network

## Methodology:

        •  Internal Network Scanning
                  traceroute www.google.com
                  nmap 192.168.1.*
        
        •  Port Scanning
                  nmap -p- -T4 -iL sub.txt (Fast Scan)
                  nmap -A 192.168.1.1 (Little Intense and slow)
                  nmap -sV -sC -Pn -p 1-65535 -T5 --min-rate 1000 --max-retries 5 192.168.1.1
                  nmap -sS -sC -sV -v -p 445 -iL subnet-files.txt
                  nmap -sS -sC -sV -v -p 21 -iL subnet-files.txt

                  Web Ports: 80, 8080, 443

                  
        •  Fingerprinting
                  nmap -sV --version-intensity 5 192.168.1.1
                  nc 192.168.1.1 80
                  curl -sI http://192.168.1.1

        •  Vulnerbility Scanning
                  nmap --script vuln 192.168.1.1 -d
                  nikto
                  dirsearch
                  nessus    (https://localhost:8834)
        
        •  IDS Penetration Testing
                  lbd 45.34.23.12
                  wafw00f http://192.168.1.1  
    
        •  SMB Enumeration
                Discover Host:
                cme smb <subnet>    (cme => crackmapexecs)

                Null Session:
                cme smb 192.168.24.0/24 -u '' -p ''
                smbmap –host-file smb-hosts.txt

                SMB Map:
                smbmap -H 192.168.1.1

        •  Exploit Research
                  https://www.exploit-db.com/
                  https://www.rapid7.com/db/
                  https://cxsecurity.com/search/       

        •  Manual Vulnerability Testing and Verification
        •  Password Strength Testing
                  rate limiting
                  sparta(tool)

        •  Infrastructure Mapping (Maltego)

                  DNS Server
                  Firewall
                  Cloud
                  Employ Device
                  Logging Server
                  Directory Service
                  Admin Workstation

        •  Common Server Misconfiguration                                                           
        •  Administrator Privileges Escalation
        •  Database Security Controls Testing    
        •  Third-Party/Vendor Security Configuration Testing



## Tool for Automation:
Internal network could possibly contain large amount of IPs,So for automation first i generate some
liner commands and then automate them.

## Requirements:
1. Currently only suppourt in Kali
2. download dirsearch and place it /haise/---> here <---

## Usage:
1. git clone https://github.com/syedumerqadri/haise.git
2. cd haise
3. put all discoverd OR provided cilient IPs on hosts.txt
4. python haise.py

You will got the prompt shell
![]()


## Shell:
		[exit]
		[clear]
		[hosts]	list all hosts
		[alive]	check if hosts are alive
		[ports]	port scan of all hosts
		[dir]	Directory Enumuration
	        [headers]  Grab Web Headers
		[scan]	Grab Headers, Port Scan and Directory Enumuration for all hosts 
		[ids] Detect Intrusion Detection System
		[smb] Check for SMB Services


## Results:
	Discoverd Web Directories: dir_results
	Discoverd Web headers: headers
    Port Scan Results: port_scan




