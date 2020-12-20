import os
import time
import random
from multiprocessing import Pool

def run(name):
    print("Child id: %s, with %s" %(os.getpid(),name))
    time.sleep(random.random())

if __name__=="__main__":
    print('Child id: %s.' % os.getpid())
    p=Pool(2)
    for i in range(10):
        p.apply_async(run,args=(i,),callback=lambda x: print("%s is done" % x))
    p.close()
    p.join()
    print("All Done.")