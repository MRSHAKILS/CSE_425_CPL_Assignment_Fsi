"""
Name: [Your Name]
Part 3: Simple Dining Philosophers
"""

import random
import threading
import time

forks = [threading.Lock() for _ in range(3)]


def philosopher(pid):
    left = pid
    right = (pid + 1) % 3

    for meal in range(1, 4):
        print(f'Philosopher {pid} is thinking (round {meal})...')
        time.sleep(random.uniform(0.6, 1.0))
        print(f'Philosopher {pid} is hungry.')

        first = min(left, right)
        second = max(left, right)

        with forks[first]:
            print(f'Philosopher {pid} picked up fork {first}.')
            with forks[second]:
                print(f'Philosopher {pid} picked up fork {second}.')
                print(f'Philosopher {pid} is eating (round {meal})...')
                time.sleep(random.uniform(0.6, 1.0))
                print(f'Philosopher {pid} finished eating (round {meal}).')

        print(f'Philosopher {pid} put down forks and continues.')


def main():
    threads = [threading.Thread(target=philosopher, args=(i,)) for i in range(3)]

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    print('All philosophers completed without deadlock.')


if __name__ == '__main__':
    main()
