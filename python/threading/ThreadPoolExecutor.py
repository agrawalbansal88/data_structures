from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time
values = [2,3,4,5,11,23,12,11,11]
def square(n):
   time.sleep(1)
   return n * n
def main():
   threads=[]
   executor =  ProcessPoolExecutor(max_workers=3)
   for val in values:
      th = executor.submit(square, val)
      threads.append(th)
   for th in threads:
      print(th.result())

# def main():
#    #with ThreadPoolExecutor(max_workers = 3) as executor:
#    with ProcessPoolExecutor(max_workers=3) as executor:
#       results = executor.map(square, values)
#    for result in results:
#       print(result)
if __name__ == '__main__':
   main()
