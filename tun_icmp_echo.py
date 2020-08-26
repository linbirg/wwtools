import tuntap
import array
import sys


def open_tun():
    tap = tuntap.TunTap(nic_type="Tun", nic_name="tun0")
    tap.config("192.168.2.82", "255.255.255.0")
    print(tap.name)
    return tap


def read(tun, size=4096):
    data = tun.read()

    if not data:
        return None
    print("rawdata:", ''.join('{:02x} '.format(x) for x in data))

    packet = tuntap.Packet(data=data)
    print("pkt_version:", packet.get_version())
    print("get_src:", packet.get_src())
    print("get_dst:", packet.get_dst())

    return data


def echo(data):
    echo_rsp = bytearray(data)
    echo_rsp[12:16] = data[16:20]
    echo_rsp[16:20] = data[12:16]

    echo_rsp[20] = 0

    ushort_22 = data[22:24]
    ushort_a = int.from_bytes(ushort_22, sys.byteorder)
    ushort_a += 8
    ushort_22_b = ushort_a.to_bytes(2, sys.byteorder)
    echo_rsp[22] = ushort_22_b[0]
    echo_rsp[23] = ushort_22_b[1]

    return bytes(echo_rsp)


def tun_icmp_echo():
    tun = open_tun()
    while True:
        data = read(tun)
        data = echo(data)
        tun.write(data)

    tun.close()


if __name__ == '__main__':
    tun_icmp_echo()
