import time
from threading import Thread


def fibonacci(num):
    if num <= 2:
        return 1
    return fibonacci(num-1) + fibonacci(num-2)


def task(num):
    print("{} : {}".format(num, fibonacci(num)))

# executor = Pool(max_workers=2)


start = time.time()

t1 = Thread(target=task, args=(40,))
t2 = Thread(target=task, args=(40,))

t1.start()
t2.start()

t1.join()
t2.join()

print "\n", time.time() - start, "seconds"
