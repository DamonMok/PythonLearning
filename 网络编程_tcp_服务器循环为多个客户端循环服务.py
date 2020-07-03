import socket


def main():
    # 1.创建tcp套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.绑定服务器端口
    tcp_server_socket.bind(("", 6789))

    # 3.将默认为主动连接的套接字变为被动连接(listen)
    tcp_server_socket.listen(128)

    # 循环为多个客户端服务
    while True:
        # 4.等待接受客户端的连接(accept)
        new_client_socket, client_address = tcp_server_socket.accept()
        print("新的客户来了，解除accept堵塞！")

        # 为一个客户端服务多次
        while True:
            # 5.接收客户端发送过来的请求
            recv_data = new_client_socket.recv(1024)

            if recv_data:
                print("接收到来自：%s 的请求数据是：%s" % (str(client_address), recv_data.decode("utf-8")))

                # 6.回送数据给客户端
                new_client_socket.send("status = 1,ok!".encode("utf-8"))
            else:
                break

        # 7.关闭套接字(一个客户端发送一次数据后就会关闭套接字)
        new_client_socket.close()

    tcp_server_socket.close()


if __name__ == '__main__':
    main()
