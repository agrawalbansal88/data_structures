# Python program to understand
# the concept of pool
import multiprocessing
import os


##############################################################
##############################################################
##############################################################
def square(n):
    print("Worker process id for {0}: {1}".format(n, os.getpid()))
    return (n * n)


def multiprocessing_Pool():
    mylist = [1,2,3,4,5]
    p = multiprocessing.Pool()
    result = p.map(square, mylist)
    print(result)

##############################################################
##############################################################
##############################################################
# function to withdraw from account
def withdraw(balance, lock):
	for _ in range(10000):
		lock.acquire()
		balance.value = balance.value - 1
		lock.release()

# function to deposit to account
def deposit(balance, lock):
	for _ in range(10000):
		lock.acquire()
		balance.value = balance.value + 1
		lock.release()

def perform_transactions():

	# initial balance (in shared memory)
	balance = multiprocessing.Value('i', 100)
	#balance = multiprocessing.Array('i', range(10)) # i: signed int, d: double precision float

	lock = multiprocessing.Lock()
	p1 = multiprocessing.Process(target=withdraw, args=(balance,lock))
	p2 = multiprocessing.Process(target=deposit, args=(balance,lock))

	p1.start()
	p2.start()
	p1.join()
	p2.join()

	# print final balance
	print("Final balance = {}".format(balance.value))

def multiprocessing_data_sharing_value():
	for _ in range(10):
		perform_transactions()

##############################################################
##############################################################
##############################################################

if __name__ == "__main__":
    multiprocessing_Pool()
    multiprocessing_data_sharing_value()
