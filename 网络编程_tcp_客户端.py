import socket


def main():
    """tcp客户端收发数据"""

    # 1.创建tcp套接字
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.与服务器建立连接
    tcp_client_socket.connect(("192.168.1.15", 6789))

    # 3.收发数据
    # 发送
    send_data = input("请输入要发送给服务器的数据：")
    tcp_client_socket.send(send_data.encode("utf-8"))

    # 接收
    recv_data = tcp_client_socket.recv(1024)  # recv_data是二进制数据
    print(recv_data.decode("utf-8"))

    # 4.关闭连接
    tcp_client_socket.close()


if __name__ == '__main__':
    main()
