import socket
import re


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
    tcp_server_socket.setblocking(False)

    # 2.绑定端口
    tcp_server_socket.bind(("", 6789))

    # 3.把套接字从主动连接变成被动连接
    tcp_server_socket.listen()

    # 5.为多个客户服务
    client_socket_list = list()  # 保存连接进来的new_client_socket

    while True:
        # 4.等待接收客户端连接
        try:
            new_client_socket, new_client_address = tcp_server_socket.accept()
        except Exception as ret:
            # 没有新的客户端到来
            pass
        else:
            # 有新的客户端到来
            new_client_socket.setblocking(False)  # 设置为非堵塞
            client_socket_list.append(new_client_socket)

        for client_socket in client_socket_list:

            try:
                # 接收浏览器的请求数据
                recv_data = client_socket.recv(1024).decode("utf-8")
            except Exception as ret:
                # 用户没有发送消息
                pass
            else:
                if recv_data:
                    service_client(client_socket, recv_data)
                else:
                    client_socket_list.remove(client_socket)

    # 6.关闭套接字
    tcp.server_socket.close()


if __name__ == '__main__':
    main()
