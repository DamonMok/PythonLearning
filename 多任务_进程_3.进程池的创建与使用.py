import multiprocessing
import time
import os
import random


def task(msg):
    start_time = time.time()
    print("%s开始执行，进程号为：%d" % (msg, os.getpid()))

    time.sleep(random.random()*2)
    end_time = time.time()
    print(msg, "执行完毕,耗时：%0.2f" % (end_time-start_time))


def main():
    """如果需要多个进程处理事情，可以使用进程池节省资源"""
    # 1.创建进程池，并制定最大进程数
    po = multiprocessing.Pool(3)

    for i in range(10):
        # 2.出入要调用的目标
        po.apply_async(task, args=(i,))

    print("---start---")

    # 3.关闭进程池，关闭后不在接收新的请求
    po.close()

    # 4.等待子进程全部执行完
    po.join()

    print("---end---")


if __name__ == '__main__':
    main()
