"""
Name: [Your Name]
Part 1: Race Condition and Basic Synchronization
"""

import threading
import time


class Counter:
    def __init__(self, use_lock=False):
        self.value = 0
        self.use_lock = use_lock
        self.lock = threading.Lock()

    def increment(self):
        if self.use_lock:
            with self.lock:
                self.value += 1
        else:
            temp = self.value
            time.sleep(0.00001)
            temp += 1
            self.value = temp


def worker(counter, times):
    for _ in range(times):
        counter.increment()


def run_test(use_lock):
    counter = Counter(use_lock=use_lock)
    threads = [threading.Thread(target=worker, args=(counter, 1000)) for _ in range(3)]

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    mode = 'WITH LOCK' if use_lock else 'WITHOUT LOCK'
    print(f'{mode}: Final counter value = {counter.value}')


if __name__ == '__main__':
    run_test(use_lock=False)
    run_test(use_lock=True)
    print('Expected value with 3 threads x 1000 increments = 3000')
