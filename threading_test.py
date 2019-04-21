import threading
import time

class MyThread(threading.Thread):
    def __init__(self,num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):
        print("running on number :%s" % self.num)

        time.sleep(3)

def Hi(num):
    print('hello %s %s ' % (num, time.time()))
    time.sleep(int(num))
    print('end %s %s ' % (num, time.time()))

if __name__ == '__main__':

    t1 = threading.Thread(target=Hi, args=(3,)) #只是创建了一个线程对象
    t1.setDaemon(True)
    t1.start()
    # t1.join()

    t2 = threading.Thread(target=Hi, args=(5,))
    #t2.setDaemon(True)
    t2.start()
    # t2.join()

    print("ending.....")