import threading
import time

def task(lock):
    print "WAITING_LOCK {}".format(threading.current_thread().name)
    with lock:
        print "GOT_LOCK {}".format(threading.current_thread().name)
        time.sleep(0.01)



t =[]
lock= threading.RLock()
for i in range(1000):
    th = threading.Thread(target=task, args=(lock,), name="THREAD_"+str(i))
    th.start()
    t.append(th)


for tt in t:
    tt.join()
