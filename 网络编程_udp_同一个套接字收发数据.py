import socket


def main():
    """同一个套接字收发数据"""
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 创建套接字
    udp_socket.bind(("", 6788))  # 绑定端口号
    udp_socket.sendto(b"Hello", ("192.168.1.10", 6789))  # 发送数据

    data = udp_socket.recvfrom(1024)  # 接收数据
    print(data[0].decode("utf-8"))

    udp_socket.close()


if __name__ == '__main__':
    main()
