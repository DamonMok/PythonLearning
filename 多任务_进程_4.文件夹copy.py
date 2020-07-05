import time
import random
import multiprocessing
import os


def copy_file(old_folder_name, new_folder_name, file_name, queue):
    """copy文件"""

    # print("从文件夹:%s 复制到文件夹:%s --->文件名字是:%s" % (old_folder_name, new_folder_name, file_name))

    # 1.从旧文件读,写入新文件
    old_f = open(old_folder_name+"/"+file_name, "rb")
    new_f = open(new_folder_name + "/" + file_name, "wb")
    while True:
        # 每次最大读入1024
        time.sleep(random.random())

        content = old_f.read(1024)

        if content:
            # 如果有内容，就写入
            new_f.write(content)
        else:
            break

    old_f.close()
    new_f.close()

    # 2.每次完成copy，都加入到队列，用以主进程显示下载进度
    queue.put(file_name)


def main():
    # 1.获取要copy的文件夹名字
    # old_folder_name = input("请输入要copy的文件夹名字:")
    old_folder_name = "old_folder"

    # 2.创建新的文件夹
    new_folder_name = "[new_copy]_"+old_folder_name
    try:
        os.mkdir(new_folder_name)
    except FileExistsError as ret:
        # print(ret)
        pass

    # 3.读取文件夹内所有文件的名字
    file_names = os.listdir("./%s" % old_folder_name)
    print(file_names)

    # 5.使用进程间通信，完成拷贝进度显示
    queue = multiprocessing.Manager().Queue()

    # 4.创建进程池
    po = multiprocessing.Pool(3)
    for file_name in file_names:
        # 往进程池添加任务
        po.apply_async(copy_file, args=(old_folder_name, new_folder_name, file_name, queue))
    po.close()

    # 进度显示
    count = 1
    while True:
        file_name = queue.get()  # 从队列中取数据，数据还没来时会阻塞

        if count > len(file_names):
            break

        print("\r已完成【%s】文件的复制，当前复制进度为:%.02f%%" % (file_name, count*100 / len(file_names)), end="")
        count += 1

    po.join()


if __name__ == '__main__':
    main()
