import time
import multiprocessing


def test1():
    for i in range(10):
        print(i)
        time.sleep(0.5)


def test2():
    for i in range(10):
        print(i)
        time.sleep(0.5)


def main():
    """Process多进程"""
    """子进程会把父进程的代码拷贝一份，各个进程间全局变量不共享"""
    p1 = multiprocessing.Process(target=test1)
    p2 = multiprocessing.Process(target=test2)

    p1.start()
    p2.start()


if __name__ == '__main__':
    main()
