from multiprocessing import Process, Value, Array, Lock
# from threading import Thread
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

def add_100(number, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        number.value += 1
        lock.release()

if __name__ == '__main__':
    lock = Lock()
    shared_number = Value('i', 0)
    print('Number at beginning is',shared_number.value)

    p1 = Process(target=add_100, args=(shared_number,lock))
    p2 = Process(target=add_100, args=(shared_number,lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('number at end is', shared_number.value)


