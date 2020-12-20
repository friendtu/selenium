import time
import random
from multiprocessing import Process,Queue

def producer(q,name):
    count=1
    while True:
        q.put("water %d" % count)
        print("%s create water %d" % (name,count))
        count+=1
        time.sleep(random.random())

def consumer(q,name):
    while True:
        print("%s consume %s."% (name,q.get()))
        time.sleep(1)

if __name__=='__main__':
    q=Queue()
    p_producer=Process(target=producer,args=(q,'Kim'))
    p_consumer=Process(target=consumer,args=(q,'lily'))
    p_producer.start()
    p_consumer.start()

    time.sleep(10)
    p_producer.terminate()
    p_consumer.terminate()
        