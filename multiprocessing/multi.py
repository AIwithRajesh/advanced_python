from multiprocessing import Process, Value, Array, Lock
# from threading import Thread
from multiprocessing import Queue
import os
import time

# print(os.cpu_count())
# processes = []
# num_processes = os.cpu_count()

# def square_numbers():
#     for i in range(100):
#         i * i

# create processes
# for i in range(num_processes):
#     p = Process(target=square_numbers)
#     processes.append(p)

# #START
# if __name__ == "__main__":
#     for p in processes:
#         p.start()

# #JOIN
# if __name__ == "__main__":
#     for p in processes:
#         p.join()

# print('end main')

# threads = []
# num_threads = 10

# for i in range(num_threads):
#     t = Thread(target=square_numbers)
#     threads.append(t)

# #START
# if __name__ == "__main__":
#     for t in threads:
#         t.start()

# #JOIN
# if __name__ == "__main__":
#     for t in threads:
#         t.join()

# print('end main')

# SHARING VALUES BETWEEN TWO PROCESSING

def add_100(numbers, lock):
    for i in range(100):
        time.sleep(0.01)
        for i in range(len(numbers)):
            with lock:
                numbers[i] += 1
        # with lock:
        #     number.value += 1

def square(numbers, queue):
    for i in numbers:
        queue.put(i*i)

def make_negative(numbers, queue):
    for i in numbers:
        queue.put(-1 * i)

if __name__ == '__main__':

    numbers = range(1,6)
    q = Queue()

    p1 = Process(target=square, args=(numbers, q))
    p2 = Process(target=make_negative, args=(numbers, q))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    while not q.empty():
        print(q.get())

    # lock = Lock()
    # # shared_number = Value('i', 0)
    # shared_array = Array('d', [0.0, 100.0,200.0])
    # print('shared_array at beginning is',shared_array[:])

    # p1 = Process(target=add_100, args=(shared_array,lock))
    # p2 = Process(target=add_100, args=(shared_array,lock))

    # p1.start()
    # p2.start()

    # p1.join()
    # p2.join()

    # print('number at end is', shared_array[:])


