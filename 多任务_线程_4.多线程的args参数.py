import time
import threading


def test(loop_times):
    for i in range(loop_times):
        print(i)
        time.sleep(0.5)


def main():
    """多线程的args参数"""
    t = threading.Thread(target=test, args=(5,))

    t.start()


if __name__ == '__main__':
    main()
