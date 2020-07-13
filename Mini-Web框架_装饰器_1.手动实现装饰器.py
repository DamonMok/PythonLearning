def set_func(func):

    def call_func():
        print("权限验证1")
        print("权限验证2")
        func()

    return call_func


# @set_func  # 这句话相当于在每次调用test1()的时候，自动在test1()的上方紧接着加上test1 = set_func(test1)
def test1():
    print("-----test1-----")


# 接收方test1指向 set_func(test1)的返回值-->call_func
test1 = set_func(test1)  # 括号的test1指向test函数
test1()  # 相当于执行call_func
