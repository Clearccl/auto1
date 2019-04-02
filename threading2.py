#coding:utf-8
from time import sleep, ctime
from threading import Thread, currentThread, activeCount

'''
多线程
'''
# 创建一个超级播放器
def super_player(name, time_long):
    for i in range(2):
        print("播放音乐：%s, %s秒" % (name, time_long), "time：%s" % ctime())
        sleep(time_long)


if __name__ == "__main__":
    # 创建播放列表
    play_list = (['好汉歌', 3], ['天下无贼', 5])
    play_num = len(play_list)
    # 创建线程
    threads = []
    for item in play_list:
        t = Thread(target=super_player, args=item)
        threads.append(t)

    # 开启线程
    for i in range(play_num):
        threads[i].start()

    # 守护线程
    for i in range(play_num):
        threads[i].join()


    print('okok')