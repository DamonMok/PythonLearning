def login():
    return "login-----"


def register():
    return "register-----"


def application(environ, start_response):

    # 1.调用web服务器传过来的函数，给服务器返回header信息
    start_response('200 OK', [('Content-Type', 'text/html;charset="utf-8"')])

    # 2.给服务器返回body信息
    path = environ['PATH_INFO']

    if path == "/index.py":
        return login()
    elif path == "/register.py":
        return register()
    else:
        return "404 not found!"
