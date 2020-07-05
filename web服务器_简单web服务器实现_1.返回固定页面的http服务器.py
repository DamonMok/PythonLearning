import socket


def service_client(new_client_socket):
    # 1.接收浏览器请求
    request = new_client_socket.recv(1024)
    print(request)

    # 2.返回数据给浏览器
    # Header
    response = "HTTP/1.1 200 OK\r\n"  # 这里必须有换行\r\n
    response += "\r\n"  # 这里必须有换行\r\n,区分Header和body

    # body
    response += "hello,hi,how are you"
    new_client_socket.send(response.encode("utf-8"))

    # 3.关闭连接
    new_client_socket.close()


def main():
    # 1.创建tcp套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.绑定端口
    tcp_server_socket.bind(("", 6788))

    # 3.把套接字从主动连接变成被动连接
    tcp_server_socket.listen()

    # 5.为多个客户服务
    while True:
        # 4.等待接收客户端连接
        new_client_socket, new_client_address = tcp_server_socket.accept()
        service_client(new_client_socket)

    # 6.关闭套接字
    tcp.server_socket.close()


if __name__ == '__main__':
    main()
