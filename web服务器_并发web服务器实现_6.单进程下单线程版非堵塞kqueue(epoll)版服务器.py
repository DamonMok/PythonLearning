import socket
import re
import select


def service_client(new_client_socket, recv_data):

    print(recv_data)

    # 1.获取请求路径
    # GET /index.html HTTP/1.1
    # 提取 /index.html
    request_lines = recv_data.splitlines()
    ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])

    file_name = ""
    if ret:
        file_name = ret.group(1)
        if file_name == "/":
            file_name = "/index.html"

    # 2.返回给浏览器的数据
    # body
    try:
        f = open("./html" + file_name, "rb")

    except (FileNotFoundError, NotADirectoryError):
        # 文件或目录不存在，响应404
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += "\r\n"
        response += "file not found!"
        new_client_socket.send(response.encode("utf-8"))

    else:
        # 文件存在
        # Body
        content = f.read()
        f.close()

        # Header
        response_header = "HTTP/1.1 200 OK\r\n"  # 这里必须有换行\r\n
        response_header += "Content-Length: %d\r\n" % len(content)
        response_header += "\r\n"  # 这里必须有换行\r\n,区分Header和body

        # 发送
        new_client_socket.send(response_header.encode("utf-8"))
        new_client_socket.send(content)

    # 3.关闭连接(如果是短连接，传完一次数据，就由服务器把套接字关掉)
    # 为了长连接，这里不主动关闭连接。使用Hearde的content的len属性，让浏览器知道什么时候传完，
    # 浏览器知道什么传完后，会自动继续向服务器发送图片等连接的请求
    # new_client_socket.close()


def main():
    # 1.创建tcp套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 把tcp_server_socket设置为非堵塞
    # tcp_server_socket.setblocking(False)

    # 2.绑定端口
    tcp_server_socket.bind(("", 6788))

    # 3.把套接字从主动连接变成被动连接
    tcp_server_socket.listen()

    # 4.为多个客户服务

    # 创建kqueue对象
    kq = select.kqueue()

    # 监听tcp_server_socket的accept()事件
    events = [
        # 有读入时，会通知
        select.kevent(tcp_server_socket.fileno(), select.KQ_FILTER_READ)
    ]

    # 把new_client_socket对象以其key存入字典中
    event_dict = dict()

    while True:

        print("等待新客户连接，正在等待通知来临！堵塞中。。。")

        # 监听到通知到来(accept())前，会堵塞，
        # 但可以并发(多个客户可以同时连接(accept)或者发送数据(send)过来)

        # event_list就是通知来的时候，有事件关联的kevent对象
        event_list = kq.control(events, 1)

        print("通知来临，有新客户连接，解除堵塞！")
        for event in event_list:
            if event.ident == tcp_server_socket.fileno():
                # 如果是有客户连接
                # event.ident代表文件描述符(fd)
                new_client_socket, new_client_address = tcp_server_socket.accept()

                # 把连接过来的客户，根据fd存入字典
                event_dict[new_client_socket.fileno()] = new_client_socket

                # 把tcp_server_socket的accept()加入监听事件
                events.append(select.kevent(new_client_socket.fileno(), select.KQ_FILTER_READ))

            elif event.filter == select.KQ_FILTER_READ:
                # 如果是有客户发送请求消息
                # 在字典中根据key接收浏览器的请求数据
                recv_data = event_dict[event.ident].recv(1024).decode("utf-8")

                if recv_data:
                    service_client(event_dict[event.ident], recv_data)
                else:
                    del event_dict[event.ident]

    # 6.关闭套接字
    tcp.server_socket.close()


if __name__ == '__main__':
    main()
