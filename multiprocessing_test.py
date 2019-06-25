
import  multiprocessing
import time

from queue import  Queue
import logging
logging.basicConfig(format='%(asctime)s : Line: %(lineno)d - %(message)s', level=logging.DEBUG)

def func1():
    def Process1(count):
        print("Process1 start")
        time.sleep(3)
        print("Process1 end")

    p= multiprocessing.Process(target=Process1, args=(count,))
    p.start()
    time.sleep(1)
    p.terminate() # terminate in middle
    p.join()


def func2_pool():
    def do_work(inp):
        return inp * 2

    def init_process():
        pass

    pool_size = multiprocessing.cpu_count()*2
    pool = multiprocessing.Pool(processes=pool_size, initializer=init_process)

    inputs = list(range(10))
    outputs=pool.map(do_work, inputs)
    print("outputs=", outputs)
    pool.close()
    pool.join()


def pipe():
    def pip1_worker1(conn):
        conn.send(("Ankur", 12))
        print("SENDER received", conn.recv())

    def pipe2_worker2(conn):
        content = conn.recv()
        print("RECEIVER", content)
        conn.send("NEW CONTENT")

    conn1, conn2 = multiprocessing.Pipe(True)
    p1 = multiprocessing.Process(target=pip1_worker1, args=(conn1,))
    p2 = multiprocessing.Process(target=pipe2_worker2, args=(conn2,))
    p1.start()
    p2.start()

def queue_test():
    def queue_hander1(que):
        que.put(10)
        time.sleep(1)
        x= que.get()
        print("Received at heander 1", x)

    def queue_hander2(que):
        print("queue_hander2 starting")
        x = que.get()
        print("Received at heander 2", x)
        que.put(11)

    que = multiprocessing.JoinableQueue()
    p1 = multiprocessing.Process(target=queue_hander1, args=(que,), name="PROCESS1")
    p2 = multiprocessing.Process(target=queue_hander2, args=(que,), name="PROCESS2")
    p1.start()
    p2.start()

def data_sharing_manager():
    def updater(lock, dictonary):
        for i in range(1,10):
            with lock:
                old_val = 0
                if i in dictonary:
                    old_val = dictonary[i]
                dictonary[i] = old_val+i*1
    manager = multiprocessing.Manager()
    d = manager.dict()
    lock = multiprocessing.Lock()
    jobs = [multiprocessing.Process(target=updater, args=(lock, d,))for _ in range(4)]
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()

    print("in parenet process",d) #{0: 0, 1: 100, 2: 200, 3: 300}

def executers():
    from concurrent.futures import ThreadPoolExecutor
    #from concurrent.futures import ProcessoolExecutor

    def do_task(dur):
        logging.debug("Sleeping for {}".format( dur))
        time.sleep(dur)
        return "Ankur" + str(dur)

    #with ProcessoolExecutor(max_workers=2) as executer:
    with ThreadPoolExecutor(max_workers=2) as executer:
        f1 = executer.submit(do_task, 2)
        f2 = executer.submit(do_task, 4)
    print(f1.result())
    print(f2.result())

if __name__ =="__main__":

    count =100
    print ("MAIN START")
    #func1()
    #func2_pool()
    #pipe()
    #queue_test()
    #data_sharing_manager()
    executers()
    print ("MAIN END")


