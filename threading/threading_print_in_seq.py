import threading
import time

# semaforo1 = threading.Semaphore(1)
# semaforo2 = threading.Semaphore(1)
# semaforo3 = threading.Semaphore(1)


def threadRed(n):
    semaforo2.acquire()
    semaforo3.acquire()
    for i in range(n):
        if i%3==0:
            semaforo1.acquire()
            print(i, end =" ")
            semaforo2.release()


def threadYellow(n):
    for i in range(n):
        if i%3==1:
            semaforo2.acquire()
            print(i,end =" ")
            semaforo3.release()



def threadGreen(n):
    for i in range(n):
        if i%3==2:
            semaforo3.acquire()
            print(i,end =" ")
            semaforo1.release()




loop_count = 100
semaforo1 = threading.Lock()
semaforo2 = threading.Lock()
semaforo3 = threading.Lock()

t_red = threading.Thread(target=threadRed, args=(loop_count,))

t_yellow = threading.Thread(target=threadYellow, args=(loop_count,))

t_green = threading.Thread(target=threadGreen, args=(loop_count,))


t_red.start()
t_yellow.start()
t_green.start()
t_red.join()
t_yellow.join()
t_green.join()
print("")



# def even(max_count, lock):
#     for i in range(max_count+1):
#         if i%2==0:
#             with lock:
#                 print i,
#                 lock.notify()
#                 if (max_count-i)>=1:
#                     lock.wait()
#
# def odd(max_count, lock):
#     for i in range(max_count+1):
#         if i%2!=0:
#             with lock:
#                 lock.wait()
#                 print i,
#                 lock.notify()
#
#
#
# lock = threading.Condition()
# t1 = threading.Thread(target=even, args=(100,lock,), name="th1")
# t2 = threading.Thread(target=odd, args=(100,lock,))
# t2.start() #odd
# t1.start() # even
#
# t1.join()
# t2.join()