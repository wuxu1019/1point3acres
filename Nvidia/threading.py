"""
https://www.geeksforgeeks.org/multithreading-python-set-1/
thread control block
process control block
all thread share global variable(stored in heap) and program code
each thread contain its own register set and local variable(stored in stack)

A race condition occurs when two or more threads can access shared data
and they try to change it at the same time.
As a result, the values of variables may be unpredictable
and vary depending on the timings of context switches of the processes.

Advantages:

It doesn’t block the user. This is because threads are independent of each other.
Better use of system resources is possible since threads execute tasks parallely.
Enhanced performance on multi-processor machines.
Multi-threaded servers and interactive GUIs use multithreading exclusively.


Disadvantages:
As number of threads increase, complexity increases.
Synchronization of shared resources (objects, data) is necessary.
It is difficult to debug, result is sometimes unpredictable.
Potential deadlocks which leads to starvation, i.e. some threads may not be served with a bad design
Constructing and synchronizing threads is CPU/memory intensive.


deadlock


"""

import threading

x = 0

def increament():

    global x
    x += 1

def thread_task(lock):

    for _ in range(10000):
        lock.aquire()
        increament()
        lock.release()

def main_task():
    global x
    x = 0

    lock = threading.Lock
    t1 = threading.Thread(target = thread_task, args=(Lock, ))
    t2 = threading.Thread(target = thread_task, args=(Lock, ))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == '__main__':
    for i in range(10):
        main_task()
        print("Iteration {0}: x = {1}".format(i, x))

