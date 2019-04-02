#coding:utf-8
import threading
from time import sleep, ctime
'''
使用自己写的线程类
'''
class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name


    def run(self):
        # apply(self.func, self.args) python2
        self.func(*self.args)


# 创建一个超级播放器
def super_player(name, time_long):
    for i in range(2):
        print("播放音乐：%s, %s秒" % (name, time_long), "time：%s" % ctime())
        sleep(time_long)

def main():
    # 创建播放列表
    play_list = (['好汉歌', 3], ['天下无贼', 5])
    play_num = len(play_list)
    # 创建线程
    threads = []
    for item in play_list:
        t = MyThread(super_player, item)
        threads.append(t)

    # 开启线程
    for i in range(play_num):
        threads[i].start()

    # 守护线程
    for i in range(play_num):
        threads[i].join()

    print('okok')

if __name__ == "__main__":
    main()