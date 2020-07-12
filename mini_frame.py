import time


def login():
    return "login--%s" % time.ctime()


def register():
    return "register--%s" % time.ctime()


def other():
    return "other--%s" % time.ctime()


def application(file_name):

    # 把逻辑代码跟web服务器解耦
    if file_name == "/login.py":
        return login()
    elif file_name == "/register.py":
        return register()
    elif file_name == "/other.py":
        return other()
    else:
        return "page not found!404!"
