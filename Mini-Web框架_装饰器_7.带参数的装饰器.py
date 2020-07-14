def out_func(level):
    print("开始传参数！")

    def set_func(func):
        print("开始装饰！")

        def call_func(*args, **kwargs):
            if level == 1:
                print("set_func权限验证1")
            else:
                print("set_func权限验证2")

            return func(*args, **kwargs)
        return call_func
    return set_func


@out_func(2)
def test():
    print("-----test-----")


# 传参和装饰在加载.py文件的时候就会进行，不受test()影响；
# 就算不执行test(),也会进行传参和装饰
test()
