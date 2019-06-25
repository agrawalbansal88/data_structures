
import threading
import time
from contextlib import contextmanager
from collections import deque
from datetime import datetime
import logging
logging.basicConfig(format='%(asctime)s : %(filename)s:%(lineno)d - %(funcName)s() %(message)s', level=logging.DEBUG)
POOL_SIZE = 3

class Connection:
    def __init__(self, conn_name):
        self.name = conn_name
        self.last_used = datetime.utcnow()
        self.user = None

    def release(self):
        logging.debug("Releasing connection {}".format(self.name))

    def check_and_refresh(self):
        logging.debug("checking connection {}".format(self.name))
        if (datetime.utcnow()- self.last_used).seconds >= 1:
            logging.debug("refreshing connection {}".format(self.name))
            self.last_used = datetime.utcnow()
            return True
        return False

    def update_last_used(self, user):
        self.user = user
        self.last_used = datetime.utcnow()

class ResourcePool:
    def __init__(self, max_conn):
        self.max_conn = max_conn
        self.lock = threading.Semaphore(POOL_SIZE)
        self.conns = deque()
        for i in range(max_conn):
            self.conns.append(Connection("conn_"+str(i)))

    @contextmanager
    def get_conn(self, user):
        with self.lock:
            with threading.Lock():
                conn = self.conns.popleft()
            conn.update_last_used(user)
            logging.debug("---------- Got resource {} {}".format(conn.name, user))
            yield conn
            logging.debug("---------- releasing resource {} {}".format(conn.name, user))
            with threading.Lock():
                self.conns.append(conn)

    def clear_connections(self):
        for conn in self.conns:
            conn.release()
        self.conns = None

    def check_connections(self):
        for i in range(POOL_SIZE):
            with self.lock:
                with threading.Lock():
                    conn = self.conns.popleft()
                is_refreshed =  conn.check_and_refresh()
                with threading.Lock():
                    self.conns.append(conn)
                if not is_refreshed:
                    break

def task(rp):
    thread_name = threading.current_thread().name
    logging.debug( "Thread {} starting".format(thread_name))
    with rp.get_conn(thread_name) as conn:
        logging.debug("---------- Work started {} {}".format(conn.name, thread_name))
        time.sleep(4)
        logging.debug("---------- Work Finished {} {}".format(conn.name, thread_name))

def watch(rp):
    global watch_rp
    while watch_rp:
        rp.check_connections()
        time.sleep(1)


watch_rp=True
threads = []
rp = ResourcePool(POOL_SIZE)
for i in range(5):
    th = threading.Thread(target=task, args=(rp,), name="TH_"+str(i))
    th.start()
    threads.append(th)

watch_th = threading.Thread(target=watch, args=(rp,))
watch_th.start()


for th in threads:
    th.join()
watch_rp=False
watch_th.join()
rp.clear_connections()
