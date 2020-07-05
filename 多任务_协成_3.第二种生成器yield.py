import time


def task1():
    while True:
        print("---task1---")
        time.sleep(0.1)
        yield


def task2():
    while True:
        print("---task2---")
        time.sleep(0.1)
        yield


def main():
    # 如果函数内有yield,就不是函数，可以看成一个生成器模板
    # 需要调用next()方法执行函数内的代码

    # 当代码遇到yield关键字，就会跳出来执行别的代码，从而完成多任务

    t1 = task1()  # 这里不会到task1()函数里面执行
    t2 = task2()  # 这里不会到task2()函数里面执行
    while True:
        next(t1)  # 到task1()函数执行，直到遇到yield停止，执行main的下一句代码：next(t2)
        next(t2)


if __name__ == '__main__':
    main()
