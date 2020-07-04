import threading
import socket


def send_msg(udp_socket):
    while True:
        send_data = input("请输入要发送的数据：")
        udp_socket.sendto(send_data.encode("utf-8"), ("192.168.1.12", 6789))


def recv_msg(udp_socket):
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print("接收到来自 %s 的数据是：%s" % (recv_data[1][0], recv_data[0].decode("gbk")))


def main():
    """多线程版udp聊天器,收发可以同时进行，不会受到接收数据时recvfrom的阻塞"""

    # 1.创建udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2.绑定端口
    udp_socket.bind(("", 6789))

    # 3.发送/接收数据
    t_send_msg = threading.Thread(target=send_msg, args=(udp_socket,))
    t_recv_msg = threading.Thread(target=recv_msg, args=(udp_socket,))

    t_send_msg.start()
    t_recv_msg.start()

    # 5.关闭套接字
    # udp_socket.close()


if __name__ == '__main__':
    main()
