import socket


def main():
    """udp接收数据"""
    # 1.创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2.绑定端口(如果不绑定端口，则使用系统默认分配的随机端口，没法接收数据)
    udp_socket.bind(("", 6789))

    # 3.接收数据
    # >>(b'HI', ('192.168.1.15', 6788))
    recv_data = udp_socket.recvfrom(1024)

    # 4.打印数据
    print(recv_data)
    # 微软系统发送过来的数据默认是用gbk编码的，所以这里要用gbk解码
    # print("接收到来自：%s 的数据为：%s" % (str(recv_data[1]), recv_data[0].decode("utf-8")))
    print("接收到来自：%s 的数据为：%s" % (str(recv_data[1]), recv_data[0].decode("gbk")))

    # 5.关闭套接字
    udp_socket.close()


if __name__ == '__main__':
    main()
