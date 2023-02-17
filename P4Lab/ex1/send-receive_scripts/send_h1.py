#!/usr/bin/env python3
import argparse
import sys
import socket
import random
import struct

from scapy.all import *

'''class PathHops(Packet):
    fields_desc = [BitField("pkt_id", 0, 64),
                   BitField("numHop", 0, 8),
                   IntField("path_id", 0),
                   BitField("which_alt_switch", 0, 32), #tells at which hop the depot will try to deviate from the primary path at a single hop. NOTE: value zero is reserved for primary path - i.e., no deviation at any hop.
                   ByteField("has_visited_depot", 0), #00000000 (0) OR 11111111 (1). I'm using 8 bits because P4 does not accept headers which are not multiple of 8
                   BitField("num_times_curr_switch", 0, 64), # 31 switches + 1 filler (ease indexation). last switch ID is the leftmost bit (the most significant one)
                   BitField("is_alt", 0, 8), #force packet to go by the alternative paths
                   BitField("is_tracker", 0, 8), #every 'X' time interval, we send a probe tracker at the primary path to see if is alive again. If so, force other incoming packets in the given flow to use its primary path. 
                   BitField("sw_overlap", 0, 32)] 
bind_layers(IP, PathHops, proto=0x45)'''

def main():
    #addr = "10.1.1.2" # l3 - 1 host
    #addr = "10.1.2.2" # l3 - 2 hosts
    addr = "10.0.2.2" # mixed - 2 hosts
    #addr = "10.0.1.1" # mixed - 1 host
    iface = "h1-eth1"
    s = conf.L2socket(iface=iface)

    print("sending on interface %s to %s" % (iface, str(addr)))

    #for _ in range(1): #number of random packets
    pkt_id = 1
    while True:
        pkt = Ether(src=get_if_hwaddr(iface), dst='ff:ff:ff:ff:ff:ff') / IP(dst=addr)
        s.send(pkt)
        pkt_id += 1
        input("Press any key to send a new packet...")
if __name__ == '__main__':
    main()