import time
import gevent
from gevent import monkey


# 自动检测耗时操作，把耗时操作全部换成经过gevent封装的方法
# 这样就不用一个个去替换原生的耗时方法
monkey.patch_all()


def task1(loop_nums):

    for i in range(loop_nums):
        print("-" * 20)
        print("---task1---")

        # gevent.sleep(1)  # 需要替换成gevent的延时才有效果，自带的time.sleep没经过封装没效果
        time.sleep(1)  # 这里有耗时，会切换


def task2(loop_nums):

    for i in range(loop_nums):
        print("-" * 20)
        print("---task2---")

        # gevent.sleep(1)  # 需要替换成gevent的延时才有效果，自带的time.sleep没经过封装没效果
        time.sleep(1)  # 这里有耗时，会切换


def main():

    """
    使用gevent完成多任务
    只要有耗时操作，就会切换任务
    """
    # 需要首先 sudo pip3 install gevent

    # 这里不会执行task1/task2函数里面的代码，因为还没遇到耗时操作
    g1 = gevent.spawn(task1, 20)
    g2 = gevent.spawn(task2, 20)

    # 这里开始就会进入到task1/task2里面执行
    g1.join()
    g2.join()


if __name__ == '__main__':
    main()


