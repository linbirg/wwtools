# from tuntap import TunTap,Pack
import time

import tuntap as ttap


def test_tun():
    tap = ttap.TunTap(nic_type="Tun", nic_name="tun0")
    tap.config("192.168.2.82", "255.255.255.0")
    print(tap.name)

    while True:
        p = tap.read()

        if not p:
            continue

        packet = ttap.Packet(data=p)
        print("pkt_version:", packet.get_version())
        if not packet.get_version() == 4:
            continue
        print('packet:', "".join('{:02x} '.format(x) for x in packet.data))

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


test_tap()

# tun = TunTap(nic_type="Tun", nic_name="tun0")
# print(tun.name,tun.ip,tun.mask)
# tap = TunTap(nic_type="Tap", nic_name="tap0")
# tap.config(ip="10.10.10.10", mask="255.255.255.0", gateway="10.10.10.254")
# print(tap.mac)

# while True:
#     try:
#         buf = tap.read()
#         print(buf)
#         time.sleep(5)
#     except Exception as e:
#         print(str(e))

# # tun.close()
# tap.close()