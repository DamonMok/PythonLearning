import socket


def main():
    """从服务端下载文件"""
    # 1.创建tcp套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.连接服务器
    tcp_socket.connect(("192.168.1.10", 6789))

    # 3.获取下载的文件名
    file_name = input("请输入需要下载的文件名：")

    # 4.将文件名发送给服务器
    tcp_socket.send(file_name.encode("utf-8"))

    # 5.接收文件中的数据
    recv_data = tcp_socket.recv(1024)

    # 6.保存接收到的数据到文件中
    if recv_data:
        with open("[新]" + file_name, "wb") as file:
            file.write(recv_data)

    # 7.关闭套接字
    tcp_socket.close()


if __name__ == '__main__':
    main()
