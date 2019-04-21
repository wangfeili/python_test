import threading
import time


def Hi(num):
    print('hello %s %s ' % (num, time.time()))
    time.sleep(3)
    print('end %s %s ' % (num, time.time()))

if __name__ == '__main__':

    t1 = threading.Thread(target=Hi, args=(10,)) #只是创建了一个线程对象
    t1.start()
    t1.join()

    t2 = threading.Thread(target=Hi, args=(9,))
    t2.start()
    t2.join()

    print("ending.....")