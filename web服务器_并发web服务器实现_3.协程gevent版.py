import socket
import re
import gevent
from gevent import monkey


monkey.patch_all()  # 把所有耗时操作替换成gevent封装过的方法解决


def service_client(new_client_socket):
    # 1.接收浏览器请求
    request = new_client_socket.recv(1024).decode("utf-8")
    print(request)

    # 获取请求路径
    # GET /index.html HTTP/1.1
    # 提取 /index.html
    request_lines = request.splitlines()
    ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])

    file_name = ""
    if ret:
        file_name = ret.group(1)
        if file_name == "/":
            file_name = "/index.html"

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
        # 2.返回给浏览器的数据
        # Header
        response = "HTTP/1.1 200 OK\r\n"  # 这里必须有换行\r\n
        response += "\r\n"  # 这里必须有换行\r\n,区分Header和body

        # Body
        content = f.read()
        f.close()

        # 发送
        new_client_socket.send(response.encode("utf-8"))
        new_client_socket.send(content)

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

        # 协程服务
        gevent.spawn(service_client, new_client_socket)


    # 6.关闭套接字
    tcp.server_socket.close()


if __name__ == '__main__':
    main()
