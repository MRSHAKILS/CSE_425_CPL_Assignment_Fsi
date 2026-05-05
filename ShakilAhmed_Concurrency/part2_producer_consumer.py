"""
Name: [Your Name]
Part 2: Producer-Consumer Problem
"""

import queue
import threading
import time

basket = queue.Queue(maxsize=5)
TOTAL_ITEMS = 12
SENTINEL = 'STOP'


def baker(name, start_index, count):
    for i in range(start_index, start_index + count):
        bread = f'Bread-{i} by {name}'
        basket.put(bread)
        print(f'{name} made {bread} | Basket size: {basket.qsize()}')
        time.sleep(0.25)


def customer(name):
    while True:
        bread = basket.get()
        if bread == SENTINEL:
            basket.task_done()
            print(f'{name} received stop signal and is leaving.')
            break

        print(f'{name} ate {bread} | Basket size: {basket.qsize()}')
        time.sleep(0.35)
        basket.task_done()


def main():
    bakers = [
        threading.Thread(target=baker, args=('Baker-1', 0, TOTAL_ITEMS // 2)),
        threading.Thread(target=baker, args=('Baker-2', TOTAL_ITEMS // 2, TOTAL_ITEMS - TOTAL_ITEMS // 2)),
    ]
    customers = [
        threading.Thread(target=customer, args=('Customer-1',)),
        threading.Thread(target=customer, args=('Customer-2',)),
    ]

    for t in customers + bakers:
        t.start()

    for t in bakers:
        t.join()

    basket.join()

    for _ in customers:
        basket.put(SENTINEL)

    for t in customers:
        t.join()

    print('Producer-consumer simulation completed gracefully.')


if __name__ == '__main__':
    main()
