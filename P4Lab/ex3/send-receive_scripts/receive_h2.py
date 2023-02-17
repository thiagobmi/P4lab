#!/usr/bin/env python3
import sys
import struct

from scapy.all import sniff, sendp, hexdump, get_if_list, get_if_hwaddr, bind_layers
from scapy.all import Packet, IPOption
from scapy.all import IP, UDP, Raw, Ether
from scapy.layers.inet import _IPOption_HDR
from scapy.fields import *

class P4Calc(Packet):
    fields_desc = [BitField("x1", 0, 32),
                    BitField("y1", 0, 32),BitField("x2", 0, 32),
                    BitField("y2", 0, 32),BitField("x3", 0, 32),
                    BitField("y3", 0, 32)]

bind_layers(IP, P4Calc, proto=0x45)


def handle_pkt(pkt):
    #print("got a packet")
    #out = pkt.show2()
    #os.system("echo str(3) + " " + str(pkt[P4Calc].x1) + " " +  str(pkt[P4Calc].y1) + " " + str(pkt[P4Calc].x2) + " " +  str(pkt[P4Calc].y2) + " " + str(pkt[P4Calc].x3) + " " +  str(pkt[P4Calc].y3) | ./a.out" );
    print(str(3) + " " + str(pkt[P4Calc].x1) + " " +  str(pkt[P4Calc].y1) + " " + str(pkt[P4Calc].x2) + " " +  str(pkt[P4Calc].y2) + " " + str(pkt[P4Calc].x3) + " " +  str(pkt[P4Calc].y3))
    #print("out: ", out)
    #out[P4Calc].x1
#    hexdump(pkt)
    sys.stdout.flush()


def main():
    iface = 'h2-eth1'
    #print("sniffing on %s" % iface)
    sys.stdout.flush()
    sniff(iface = iface,
          prn = lambda x: handle_pkt(x))


if __name__ == '__main__':
    main()

