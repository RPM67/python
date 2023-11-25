import threading
import time
from concurrent.futures import ThreadPoolExecutor


def my_func(name):
  print(f"Hello from thread by {name}", threading.current_thread().name)

thread = threading.Thread(target=my_func,args=['rpm'])
thread.start()
thread.join()

thread = threading.Thread(target=my_func,args=['rohit'])
thread.start()
thread.join()


# Indicates some task being done
def func(seconds):
  print(f"Sleeping for {seconds} seconds")
  time.sleep(seconds)
  return seconds

def main():
  time1 = time.time()
  # Normal Code
  # func(4) 
  # func(2)
  # func(1)
  
  
  # Same code using Threads
  t1 = threading.Thread(target=func, args=[4])
  t2 = threading.Thread(target=func, args=[2])
  t3 = threading.Thread(target=func, args=[1])
  t1.start()
  t2.start()
  t3.start()
  
  t1.join()
  t2.join()
  t3.join()
  # Calculating Time 
  time2 = time.time()
  print(time2 - time1)


def poolingDemo():
  with ThreadPoolExecutor() as executor:
    # future1 = executor.submit(func, 3)
    # future2 = executor.submit(func, 2)
    # future3 = executor.submit(func, 4)
    # print(future1.result())
    # print(future2.result())
    # print(future3.result())
    l = [3, 5, 1, 2]
    results = executor.map(func, l)
    for result in results:
      print(result)

main()
poolingDemo()