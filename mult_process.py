#coding:utf-8
import multiprocessing
from time import sleep, ctime

'''
多进程
'''
# 创建一个超级播放器
def super_player(name, time_long):
    for i in range(2):
        print("播放：%s, %s秒" % (name, time_long), "time：%s" % ctime())
        sleep(time_long)


def main():
    # 创建播放列表
    play_list = (['好汉歌', 3], ['天下无贼', 5])
    play_num = len(play_list)
    # 创建线程
    process1 = []
    for item in play_list:
        t = multiprocessing.Process(target=super_player, args=item)
        process1.append(t)

    # 开启线程
    for i in range(play_num):
        process1[i].start()

    # 守护线程
    for i in range(play_num):
        process1[i].join()

    print('okok')


if __name__ == '__main__':
    main()

