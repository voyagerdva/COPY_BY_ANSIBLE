#!/usr/bin/python3

import os
import sys

def readCurrIndex(indexFile):
    with open(indexFile, "r") as f:
        for index in f.readlines():
            return index


def readHostsAddr(hostList):
    allHosts = []
    index = int(readCurrIndex("index.txt"))
    with open(hostList, "r") as f:
        for line in f.readlines():
            allHosts.append(line)
    if int(index) >= len(allHosts):
        index = 0
    return len(allHosts), allHosts[int(index)], index
    

def makeInventory(hostsFile, ip_address):
    with open(hostsFile, "w") as f:
        text = "[redhat]" + "\n" + ip_address
        f.write(text)
        
        
def copyWithAnsible():
    os.system("ansible all -m shell -a 'uptime'")


def writeToHostDone(hostDoneFile, index, ip_address):
    with open(hostDoneFile, "a") as f:
        line = str(index) + "\t" + str(ip_address + "\n")
        f.write(line)


def increaseIndex(index, indexFile):
    index += 1
    with open(indexFile, "w") as f:
        f.write(str(index))
    
########################################################################

maxHosts = readHostsAddr("host_list.txt")
ip_address = maxHosts[1].split('\n')[0]
index = maxHosts[2]
makeInventory("hosts", ip_address)
copyWithAnsible()
writeToHostDone("Hosts_DONE.txt", index, ip_address)
increaseIndex(index, "index.txt")
