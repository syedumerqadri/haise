ext="php,jsp,rb,py,js,asp,aspx,zip,sql,tar,txt,key,doc,docx,html,jar,groovy,back,xml,ini,inc,config,json,yml,conf,cgi"
cat hosts.txt | while read ip
do
	python3 /root/Syed\ Umer/Ebryx/project/Internal\ Network\ Pentest/tool/dirsearch/dirsearch.py -u https://$ip -e $ext -x 400,500 -t 25 --plain-text-report=https-report/http:$ip.txt
done

# cat hosts.txt | xargs -I{}  python3 dirsearch/dirsearch.py -u http://{} -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt  -e php,jsp,rb,py,js,asp,aspx,zip,sql,tar,txt,key,doc,docx,html,jar,groovy,back,xml,ini,inc,config,json,yml,conf,cgi --plain-text-report=https-report/http:{}.txt