#coding:utf-8
from time import sleep, ctime
from threading import Thread, currentThread, activeCount


def music(*args):
    for i in range(3):
        print("播放音乐：%s, %s秒" % args, "time：%s" % ctime())
        sleep(3)


def movie(*args):
    for i in range(3):
        print("播放电影：%s, %s秒" % args, "time：%s" % ctime())
        sleep(2)

if __name__ == '__main__':
    # music('好汉歌', 2)
    # movie('天下无贼', 3)
# Thread是线程类，有两种使用方法，直接传入要运行的方法或从Thread继承并覆盖run()：
#     创建线程
    threads = []
    t1 = Thread(target=music, args=('好汉歌', 2))
    t2 = Thread(target=movie, args=('天下无贼', 3))
    threads.append(t1)
    threads.append(t2)
#     启动线程
    for t in threads:
        t.start()
#     守护线程
    for t in threads:
        t.join()

    print('okok')
