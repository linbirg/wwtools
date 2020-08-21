from tuntap import TunTap
import time

# tun = TunTap(nic_type="Tun", nic_name="tun0")
# print(tun.name,tun.ip,tun.mask)
tap = TunTap(nic_type="Tap", nic_name="tap0")
tap.config(ip="10.10.10.10", mask="255.255.255.0", gateway="10.10.10.254")
print(tap.mac)

while True:
    try:
        buf = tap.read()
        print(buf)
        time.sleep(5)
    except Exception as e:
        print(str(e))

# tun.close()
tap.close()