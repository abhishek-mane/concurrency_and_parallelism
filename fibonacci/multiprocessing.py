import time
from multiprocessing import Process


def fibonacci(num):
    if num <= 2:
        return 1
    return fibonacci(num-1) + fibonacci(num-2)


def task(num):
    print("{} : {}".format(num, fibonacci(num)))

# executor = Pool(max_workers=2)


start = time.time()

p1 = Process(target=task, args=(40,))
p2 = Process(target=task, args=(40,))

p1.start()
p2.start()

p1.join()
p2.join()

print "\n", time.time() - start, "seconds"
