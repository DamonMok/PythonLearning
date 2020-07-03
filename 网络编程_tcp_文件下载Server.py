import socket


def send_file_2_client(new_client_socket, client_address):
    """发送文件给客户端"""
    # 1.接收来自客户端的文件名
    file_name = new_client_socket.recv(1024)
    print("接收到来自客户端：%s 的下载文件请求！" % str(client_address))

    # 2.根据文件名读出文件数据
    file_content = None
    try:
        f = open(file_name, "rb")
    except IOError:
        print("找不到名为：%s 的文件" % file_name.decode("utf-8"))
    else:
        file_content = f.read()
        f.close()

    # 3.发送文件数据给客户端
    if file_content:
        # 如果读取到文件，就发送给客户端
        new_client_socket.send(file_content)


def main():
    """下载文件Server"""
    # 1.创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.绑定端口
    udp_socket.bind(("192.168.1.10", 6789))

    # 3.把套接字从主动变成被动连接
    udp_socket.listen(128)

    # 4.等待接收客户端的请求
    new_client_socket, client_address = udp_socket.accept()

    # 5.给客户端返回文件数据
    send_file_2_client(new_client_socket, client_address)

    # 6.关闭套接字
    new_client_socket.close()
    udp_socket.close()


if __name__ == '__main__':
    main()
