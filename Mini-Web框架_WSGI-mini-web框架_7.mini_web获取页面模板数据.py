import socket
import re
import multiprocessing
import time
import dynamic.mini_frame4


class WSGIServer(object):

    def __init__(self):
        # 1.创建tcp套接字
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 如果服务器先断开，会保存资源几分钟。如果马上启动，端口就会被占用。加上这句话可重用。
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # 2.绑定端口
        self.tcp_server_socket.bind(("", 6788))

        # 3.把套接字从主动连接变成被动连接
        self.tcp_server_socket.listen()

        self.status = None
        self.headers = None

    def service_client(self, new_client_socket):
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

        # 2. 返回http格式的数据，给浏览器
        if not file_name.endswith(".py"):
            # 2.1 如果请求的资源不是以.py结尾的，就加载静态资源(html/css/js/png/jpg等)
            try:
                f = open("./static" + file_name, "rb")

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

        else:
            # 2.2 如果路径以.py结尾，则加载动态资源(动态解析)
            # body
            environ = dict()
            environ['PATH_INFO'] = file_name
            body = dynamic.mini_frame4.application(environ, self.set_response_header)

            # header
            header = "HTTP/1.1 %s\r\n" % self.status
            for h in self.headers:
                header += "%s:%s\r\n" % (h[0], h[1])
            header += "\r\n"

            response = header + body
            print("???????????%s" % response)
            new_client_socket.send(response.encode("utf-8"))

        # 3.关闭连接
        new_client_socket.close()  # 这是关闭子进程的new_client_socket的，因为子进程会复制父进程

    def set_response_header(self, status, headers):

        self.status = status
        self.headers = [('server', 'mini_frame1.0')]
        self.headers += headers

        print(headers)

    def run_forever(self):

        # 5.为多个客户服务
        while True:
            # 4.等待接收客户端连接
            new_client_socket, new_client_address = self.tcp_server_socket.accept()

            # 多进程服务
            p = multiprocessing.Process(target=self.service_client, args=(new_client_socket,))
            p.start()

            new_client_socket.close()  # 这是关闭父进程new_client_socket的

        # 6.关闭套接字
        self.tcp.server_socket.close()


def main():
    # 1.创建一个WSGI对象，然后调用这个对象的run_forever方法运行
    wsgi_server = WSGIServer()
    wsgi_server.run_forever()


if __name__ == '__main__':
    main()
