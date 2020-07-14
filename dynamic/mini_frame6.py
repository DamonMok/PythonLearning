URL_FUNC_DICT = dict()


def route(url):

    def set_func(func):
        URL_FUNC_DICT[url] = func

        def call_func():
            pass
        return call_func()
    return set_func


@route("/index.py")
def index():
    with open("./templates/index.html", "r") as f:
        content = f.read()
        return content


@route("/center.py")
def center():
    with open("./templates/center.html", "r") as f:
        content = f.read()
        return content


def application(environ, start_response):

    # 1.调用web服务器传过来的函数，给服务器返回header信息
    start_response('200 OK', [('Content-Type', 'text/html;charset="utf-8"')])

    # 2.给服务器返回body信息
    file_name = environ['PATH_INFO']

    try:
        func = URL_FUNC_DICT[file_name]
        return func()
    except Exception as ret:
        return "产生了异常：%s" % str(ret)
