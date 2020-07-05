import socket
import time

def main():
    # 1.创建tcp套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 设置成非堵塞后，accept不会堵塞，没有客户端连接时会抛出异常
    tcp_server_socket.setblocking(False)

    # 2.绑定服务器端口
    tcp_server_socket.bind(("", 6789))

    # 3.将默认为主动连接的套接字变为被动连接(listen)
    tcp_server_socket.listen(128)

    # 循环为多个客户端服务
    client_socket_list = list()  # 保存连接进来的客户端
    while True:

        # time.sleep(0.5)  # 为了方便查看数据，可以设置延时

        # 4.等待接受客户端的连接(accept)
        try:
            new_client_socket, client_address = tcp_server_socket.accept()

        except Exception as ret:
            print("---没有新的客户端到来---")

        else:
            print("---【有新的客户端连接来了】---")
            new_client_socket.setblocking(False)
            client_socket_list.append(new_client_socket)

        for client_socket in client_socket_list:
            try:
                recv_data = new_client_socket.recv(1024)
            except Exception as ret:
                print("---客户端没有发送数据---")
            else:
                if recv_data:
                    print("【接收到来自：%s 的请求数据是：%s】" % (str(client_address), recv_data.decode("utf-8")))
                else:
                    client_socket.close()
                    client_socket_list.remove(client_socket)
                    print("---客户端已经关闭---")

    tcp_server_socket.close()


if __name__ == '__main__':
    main()
