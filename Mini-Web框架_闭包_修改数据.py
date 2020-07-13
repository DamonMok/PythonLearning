
# 闭包：inner可以使用【外部(wrapper)的变量】，再加上inner内部的【代码】，组成一个新的整体空间，就叫闭包

num = 300


def wrapper():

    num = 200

    def inner():
        nonlocal num
        print(num)
        num = 100
        print(num)
    return inner


test = wrapper()
test()
