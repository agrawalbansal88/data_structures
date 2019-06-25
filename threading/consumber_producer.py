

import threading
import Queue

import time

def Consumber_task(que):
    print "CONSUMBER STARTING"
    while not que.empty():
        item = que.get()
        time.sleep(0.2)
        print "consumber got item", item
    print "CONSUMBER ENDED"


def producer_task(que):
    for i in range(10):
        time.sleep(0.1)
        print "Producing item", i
        que.put(i)


que = Queue.Queue(3)
consumber1 = threading.Thread(target=Consumber_task, args=(que,))
consumber2 = threading.Thread(target=Consumber_task, args=(que,))
producer = threading.Thread(target=producer_task, args=(que,))

producer.start()
time.sleep(0.2)
consumber1.start()
consumber2.start()

consumber1.join()
consumber2.join()
producer.join()




