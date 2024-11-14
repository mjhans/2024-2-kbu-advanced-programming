# linux : time python thread_test.py
# mac   : gtime python thread_test.py

from threading import Thread
import random
import time
import sys

def work(id, end):
    cnt = 1
    while (cnt <= end):    
        cnt += random.randint(0,5)
        time.sleep(0.00001)
    
if __name__ == "__main__":
    args = sys.argv[1:]
    list_count = int(args[0])
    END = 100_000

    thread_list = []
    for i in range(list_count):
        t = Thread(target=work, args=(i, int(END/list_count)))
        t.start()
        thread_list.append(t)
    
    start = time.time()
    for t in thread_list:        
        t.join()
    
    end = time.time()
    print(f"elapsed time(sec) : {end - start:.5f}")
    
    