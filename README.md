# ARP-Poison-Python
A program written in python that can poison the ARP cache of targets for a MITM attack


This program uses Scapy to create and send the malicious ARP packets

$ pip install --pre scapy[basic]


You will need the IP and MAC address of your Target and the Gateway

I recommend using a tool like Nmap to find these using a command like
nmap -T4 -F 192.168.x.x/24


Edit the script to insert your IP and MAC addresses


run with "sudo python3 arp.py"

To see the MITM attack in action, open up a Network Sniffer like WireShark to capture network traffic

Filter with ip.src == 192.168.x.x or ip.dst == 192.168.x.x
Both IP addresses being that of the Target IP address
