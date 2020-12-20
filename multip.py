import os
from multiprocessing import Process

class SubProcess(Process):
    def __init__(self,*args,**kargs):
        super(SubProcess,self).__init__()
        self.name=args[0]
    def run(self):
        print('module name:',__name__)
        print("child id: %s, with %s" % (os.getpid(),self.name))

def run(name):
    print('module name:',__name__)
    print("child id: %s, with %s" % (os.getpid(),name))

#if __name__=='__main__':
if True:
    print("parent id: %s" % os.getpid())
    p=Process(target=run,args=('test',))
    p.start()
    p.join()

    p=SubProcess("subprocess")
    p.start()
    p.join()