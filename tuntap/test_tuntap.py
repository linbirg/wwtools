# from tuntap import TunTap,Pack
import time

import tuntap as ttap
import ip_parser as ip


def test_tun():
    tap = ttap.TunTap(nic_type="Tun", nic_name="tun0")
    tap.config("192.168.2.82", "255.255.255.0")
    print(tap.name)

    parser = ip.IPParser()

    while True:
        p = tap.read()

        if not p:
            continue

        ip_header = parser.parse(p)
        print(ip_header)
        packet = ttap.Packet(data=p)
        # print("pkt_version:", packet.get_version())
        # print("get_src:", packet.get_src())
        # print("get_dst:", packet.get_dst())
        # # print("get_protocol:", packet.get_protocol())
        # if not packet.get_version() == 4:
        #     continue
        print('packet:', "".join('{:02x} '.format(x) for x in packet.data))
        print('packet str:', packet.data)

        time.sleep(5)


def test_tap():
    tap = ttap.TunTap(nic_type="Tap", nic_name="tap0")
    tap.config("192.168.2.82", "255.255.255.0")
    print(tap.name)

    while True:
        p = tap.read()

        if not p:
            continue

        packet = ttap.Packet(frame=p)
        print("pkt_version:", packet.get_version())
        if not packet.get_version() == 4:
            continue
        print('packet:', "".join('{:02x} '.format(x) for x in packet.data))

        time.sleep(5)


test_tun()
