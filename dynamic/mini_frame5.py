
def index():
    with open("./templates/index.html", "r") as f:
        content = f.read()
        return content


def center():
    with open("./templates/center.html", "r") as f:
        content = f.read()
        return content


URL_FUNC_DICT = {
    '/index.py': index,
    '/center.py': center
}


def application(environ, start_response):

    # 1.调用web服务器传过来的函数，给服务器返回header信息
    start_response('200 OK', [('Content-Type', 'text/html;charset="utf-8"')])

    # 2.给服务器返回body信息
    file_name = environ['PATH_INFO']

    func = URL_FUNC_DICT[file_name]
    return func()
