import urllib3
import multiprocessing.pool
import time
import os

number_of_processes=30
nmap_directory_name="port_scan"

def runScan(target):
    print("Target scanning: "+target)
    result = os.popen('nmap -Pn -T4 -sC -sS -sV -v -A -oA '+nmap_directory_name+'/nmap-' + target + " " + target).read().splitlines()


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


if __name__ == "__main__":
    print(" ***** nmapScanner Started ***** ")
    if not os.path.exists(nmap_directory_name):
        os.makedirs(nmap_directory_name)

    input_file = open("hosts.txt", "r")
    targets = input_file.readlines()
    input_file.close()
    targets = [x.strip() for x in targets]

    if len(targets) < number_of_processes:
        number_of_processes = len(targets)

    index = 0
    processes = []
    for i in range(number_of_processes):
        processes.append(multiprocessing.Process(target=runScan,args=(targets[index],)))
        index+=1

    for p in processes:
        p.start()

    more_loop = True
    while more_loop:
        time.sleep(5)

        for i in range(0,number_of_processes) :
            if processes[i].is_alive():
                processes[i].join(1)
                #print("jobs is not finished")
            else:
                if index >= len(targets):
                    for p in processes:
                        p.join()
                    more_loop = False
                    break
                processes[i] = multiprocessing.Process(target=runScan,args=(targets[index],))
                processes[i].start()
                index+=1

    print("Port Scan Complete !!!")
    exit(0)
