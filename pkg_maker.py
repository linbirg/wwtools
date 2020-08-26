import socket
import sys
import time
import struct

# HOST, PORT = "10.60.66.66", 10086


def make_forward_iphdr(source_ip='1.0.0.1',
                       dest_ip='2.0.0.2',
                       proto=socket.IPPROTO_UDP):
    # ip header fields
    ip_ihl = 5
    ip_ver = 4
    ip_tos = 0
    ip_tot_len = 0  # kernel will fill the correct total length
    ip_id = 54321  #Id of this packet
    ip_frag_off = 0
    ip_ttl = 255
    ip_proto = proto
    ip_check = 0  # kernel will fill the correct checksum
    ip_saddr = socket.inet_aton(
        source_ip)  #Spoof the source ip address if you want to
    ip_daddr = socket.inet_aton(dest_ip)

    ip_ihl_ver = (ip_ver << 4) + ip_ihl

    # the ! in the pack format string means network order
    ip_header = struct.pack('!BBHHHBBH4s4s', ip_ihl_ver, ip_tos, ip_tot_len,
                            ip_id, ip_frag_off, ip_ttl, ip_proto, ip_check,
                            ip_saddr, ip_daddr)
    return ip_header


def make_forward_udphdr(src_port=1024, dst_port=10086):
    udp_header = struct.pack('!HHHH', src_port, dst_port, 0, 0)
    return udp_header


# checksum functions needed for calculation checksum
def checksum(msg):
    s = 0

    # loop taking 2 characters at a time
    for i in range(0, len(msg), 2):
        w = ord(msg[i]) + (ord(msg[i + 1]) << 8)
        s = s + w

    s = (s >> 16) + (s & 0xffff)
    s = s + (s >> 16)

    #complement and mask to 4 byte short
    s = ~s & 0xffff

    return s


def make_tcp_data(ip_header,
                  src_port=1024,
                  dst_port=10086,
                  source_ip='1.0.0.1',
                  dest_ip='2.0.0.2',
                  user_data='test'):
    tcp_source = src_port  # source port
    tcp_dest = dst_port  # destination port
    tcp_seq = 454
    tcp_ack_seq = 0
    tcp_doff = 5  #4 bit field, size of tcp header, 5 * 4 = 20 bytes
    #tcp flags
    tcp_fin = 0
    tcp_syn = 1
    tcp_rst = 0
    tcp_psh = 0
    tcp_ack = 0
    tcp_urg = 0
    tcp_window = socket.htons(5840)  #   maximum allowed window size
    tcp_check = 0
    tcp_urg_ptr = 0

    tcp_offset_res = (tcp_doff << 4) + 0
    tcp_flags = tcp_fin + (tcp_syn << 1) + (tcp_rst << 2) + (tcp_psh << 3) + (
        tcp_ack << 4) + (tcp_urg << 5)

    # the ! in the pack format string means network order
    tcp_header = struct.pack('!HHLLBBHHH', tcp_source, tcp_dest, tcp_seq,
                             tcp_ack_seq, tcp_offset_res, tcp_flags,
                             tcp_window, tcp_check, tcp_urg_ptr)

    source_address = socket.inet_aton(source_ip)
    dest_address = socket.inet_aton(dest_ip)
    placeholder = 0
    protocol = socket.IPPROTO_TCP
    tcp_length = len(tcp_header) + len(user_data)

    psh = struct.pack('!4s4sBBH', source_address, dest_address, placeholder,
                      protocol, tcp_length)
    psh = psh + tcp_header + user_data

    tcp_check = checksum(psh)
    #print tcp_checksum

    # make the tcp header again and fill the correct checksum - remember checksum is NOT in network byte order
    tcp_header = struct.pack(
        '!HHLLBBH', tcp_source, tcp_dest, tcp_seq, tcp_ack_seq, tcp_offset_res,
        tcp_flags, tcp_window) + struct.pack('H', tcp_check) + struct.pack(
            '!H', tcp_urg_ptr)

    # final full packet - syn packets dont have any data
    packet = ip_header + tcp_header + user_data
    return packet