import socket


def main():
    # 1.创建udp套接字
    upd_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2.发送数据
    # 传入对方的IP、端口
    send_data = input("请输入发送的内容：")  # 发送的内容需要通过encode()转换成二进制
    upd_socket.sendto(send_data.encode("utf-8"), ("192.168.13.129", 6789))

    # 3.关闭套接字
    upd_socket.close()


if __name__ == '__main__':
    main()
