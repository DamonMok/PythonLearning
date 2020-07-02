import socket


def send_msg(udp_socket):
    """发送消息"""
    dest_ip = input("请输入对方ip:")
    dest_port = int(input("请输入对方端口："))
    send_data = input("请输入要发送的消息：")
    udp_socket.sendto(send_data.encode("utf-8"),(dest_ip, dest_port))


def recv_msg(udp_socket):
    """接收消息"""
    recv_data = udp_socket.recvfrom(1024)
    print(recv_data)
    print("接收到来自：%s 发来的数据：%s" % (str(recv_data[1]), recv_data[0].decode("gbk")))


def main():
    """udp聊天器"""

    # 1.创建收发消息套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("", 6789))

    # 2.循环处理事件
    while True:
        print("------------聊天器------------")
        print("1:发送消息")
        print("2:接收消息")
        print("0:退出")
        op = input("请选择功能：")

        if op == "1":
            # 发送消息
            send_msg(udp_socket)
        elif op == "2":
            # 接收消息
            recv_msg(udp_socket)
        elif op == "0":
            # 退出
            break
        else:
            print("输入有误，请重新输入！")
    # 3.关闭套接字


if __name__ == '__main__':
    main()

