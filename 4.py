# -*- coding: UTF-8 -*-
import schedule
import time

def count1():
    print("第一次拍照人数6人")
def count2():
    print("第二次拍照人数6人")
def count3():
    print("第三次拍照人数6人")
schedule.every(5).seconds.do(count1)
schedule.every(8).seconds.do(count2)
schedule.every(10).seconds.do(count3)
while True:
    schedule.run_pending()
    time.sleep(1)

