# from multiprocessing import Process
from threading import Thread
import os

# print(os.cpu_count())
# processes = []
# num_processes = os.cpu_count()

def square_numbers():
    for i in range(100):
        i * i

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

threads = []
num_threads = 10

for i in range(num_threads):
    t = Thread(target=square_numbers)
    threads.append(t)

#START
if __name__ == "__main__":
    for t in threads:
        t.start()

#JOIN
if __name__ == "__main__":
    for t in threads:
        t.join()

print('end main')