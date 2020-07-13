def set_func(func):

    def call_func(*args, **kwargs):
        print("权限验证1")
        print("权限验证2")
        func(*args, **kwargs)
    return call_func


@set_func
def test1(num, *args, **kwargs):
    print("-----test1-----%d", num)
    print("-----test1-----%d", args)
    print("-----test1-----%d", kwargs)


test1(100)
print("")
test1(100, 200)
print("")
test1(100, 200, 300, kw="100")
