import socket
import time


def mock_send_to(ip='192.168.2.82', port=7878):
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 读取输入的数据
    send_data = 'hello, i m mock udp!'

    # 发送数据
    send_addr = (ip, port)
    udp_socket.sendto(send_data.encode('utf-8'), send_addr)

    # 关闭
    udp_socket.close()


def main():
    while True:
        mock_send_to()
        time.sleep(4)


if __name__ == '__main__':
    main()
