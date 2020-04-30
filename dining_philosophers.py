import threading
from time import *

s0=threading.Semaphore(1)
s1=threading.Semaphore(1)
s2=threading.Semaphore(1)
s3=threading.Semaphore(1)
s4=threading.Semaphore(1)
sem=[s0,s1,s2,s3,s4]

class philosopher():
    def take_fork(self,s):
        s.acquire()

    def put_fork(self,s):
        s.release()
    def phil(self,i,name, semaphore):
        s=semaphore
        fork_left = i
        fork_right = (i + 1)%5

        #print(name)
        #print(i)
        #print(f'fork left={fork_left}')
        #print(f'fork left={fork_right}')

        print(f'{name} thinking')
        sleep(2)
        self.take_fork(sem[fork_left])
        self.take_fork(sem[fork_right])
        print(f'Crital are:{name} is eating eating')

        self.put_fork(sem[fork_left])
        self.put_fork(sem[fork_right])
class main():
    p = philosopher()
    global s0
    global s1
    global s2
    global s3
    global s4

    p0=threading.Thread(target=p.phil(i=0,name='P0',semaphore=s0))
    p1 = threading.Thread(target=p.phil(i=1,name='P1',semaphore=s1))
    p2 = threading.Thread(target=p.phil(i=2, name='P2', semaphore=s2))
    p3 = threading.Thread(target=p.phil(i=3, name='P3', semaphore=s3))
    p4 = threading.Thread(target=p.phil(i=4, name='P4', semaphore=s4))

    p0.start()
    sleep(0.2)
    p1.start()
    sleep(0.2)
    p2.start()
    sleep(0.2)
    p3.start()
    sleep(0.2)
    p4.start()
