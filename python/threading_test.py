import threading
import time

x=0

def funcLOCK():
    def thread_task1(lock):
        print (threading.current_thread(), threading.get_ident())
        global x
        mydata = threading.local()  # its an object you can fill whatever you wnat
        for i in range(1000000):
            lock.acquire()
            x += 1
            lock.release()

    def thread_task2(lock):
        print (threading.current_thread(), threading.get_ident())
        global x
        for i in range(1000000):
            with lock:
                x += 1
    lock = threading.Lock()
    t1 = threading.Thread(target=thread_task1, args=(lock,), name="Ankur_thread_1")
    t2 = threading.Thread(target=thread_task2, args=(lock,), name="I do not have any name")
    print (threading.current_thread(), threading.get_ident())
    print ("ACTIVE THREAD BEFORE START", threading.active_count())
    t1.start()
    t2.start()
    print ("ACTIVE THREAD BEFORE START", threading.active_count())

    t1.join(timeout=0.001)
    t2.join(timeout=0.001)
    print ("ACTIVE THREAD BEFORE START", threading.active_count())

def funcRLOCK():
    def thread_task3(lock):
        # acquire and release count shall be same

        print("THREAD 3 started")
        time.sleep(0.1)
        lock.acquire()
        print("THREAD 3 locked")
        time.sleep(0.5)
        lock.acquire()
        print("THREAD 3 locked again")
        time.sleep(0.5)
        lock.release()
        lock.release()

    def thread_task4(lock):
        print("THREAD 4 started")
        time.sleep(0.2)
        lock.acquire()
        print("THREAD 4 locked")
        time.sleep(1)
        lock.release()

    lock = threading.RLock()
    t3 = threading.Thread(target=thread_task3, args=(lock,), name="Ankur_thread_1")
    t4 = threading.Thread(target=thread_task4, args=(lock,), name="I do not have any name")

    t3.start()
    t4.start()
    t3.join()
    t4.join()



def funcSemaphore():
    def sema1(lock):
        time.sleep(0.5)
        lock.acquire()
        print("SEMA 1 lock 1 taken")
        time.sleep(0.3)
        lock.acquire()
        print("SEMA 1 lock 2 taken")
        lock.release()

    def sema2(lock):
        time.sleep(0.6)
        lock.acquire()
        print("SEMA 2 lock 1 taken")
        lock.release()

    lock = threading.Semaphore(2)
    t1 = threading.Thread(target=sema1, args=(lock,))
    t2 = threading.Thread(target=sema2, args=(lock,))
    #t3 = threading.Thread(target=sema3, args=(lock,))
    #t4 = threading.Thread(target=sema4, args=(lock,))

    t1.start()
    t2.start()
    #t3.start()
    #t4.start()

    t1.join()
    t2.join()
    #t3.join()
    #t4.join()

from queue import Queue

def producer(que):
    for i in range(10):
        time.sleep(0.2)
        que.put(i)
        print ("producting item ", i)
    que.put(None)# to end it

def consumer(que):
    while True:
        item = que.get()
        if item == None:
            print("------ consumed all items")
            break
        time.sleep(0.5)
        print ("consuming item ", item)
        que.task_done()


def funcQueue():
    que = Queue(2)
    t1 = threading.Thread(target=producer, args=(que,))
    t2 = threading.Thread(target=consumer, args=(que,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ =="__main__":
    print("main started")
    #funcLOCK()
    #print("x=", x)
    #funcRLOCK()
    #funcSemaphore()
    #threading.Event
    #threading.Condition
    funcQueue()
    print ("main finished")
