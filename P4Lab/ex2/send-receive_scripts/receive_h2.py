#!/usr/bin/env python3
import sys
import struct

from scapy.all import sniff, sendp, hexdump, get_if_list, get_if_hwaddr, bind_layers
from scapy.all import Packet, IPOption
from scapy.all import IP, UDP, Raw, Ether
from scapy.layers.inet import _IPOption_HDR
from scapy.fields import *

class P4Calc(Packet):
    fields_desc = [BitField("a", 0, 32),
                   BitField("b", 0, 32),
                   BitField("op", 0, 32),
                   BitField("res", 0, 32)]
bind_layers(IP, P4Calc, proto=0x45)


def handle_pkt(pkt):
    #print("got a packet")
    pkt.show2()
#    hexdump(pkt)
    sys.stdout.flush()


def main():
    iface = 'h2-eth1'
    print("sniffing on %s" % iface)
    sys.stdout.flush()
    sniff(iface = iface,
          prn = lambda x: handle_pkt(x))


if __name__ == '__main__':
    main()

