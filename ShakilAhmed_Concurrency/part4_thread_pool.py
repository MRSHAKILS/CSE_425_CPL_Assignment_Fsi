"""
Name: Shakil Ahmed
Part 4: Thread Pool for Parallel Tasks
"""

import concurrent.futures
import math
import random
import threading
import time


def process_task(task_id):
    thread_name = threading.current_thread().name
    n = random.randint(5000, 9000)
    result = math.factorial(300)
    time.sleep(random.uniform(0.25, 0.6))
    return f'Task {task_id:02d} processed by {thread_name} | count={n} | fact_digits={len(str(result))}'


def sequential_run(task_ids):
    start = time.perf_counter()
    outputs = [process_task(task_id) for task_id in task_ids]
    total = time.perf_counter() - start
    return outputs, total


def parallel_run(task_ids, workers=4):
    start = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        outputs = list(executor.map(process_task, task_ids))
    total = time.perf_counter() - start
    return outputs, total


def main():
    task_ids = list(range(10))

    print('Sequential Execution:')
    seq_outputs, seq_time = sequential_run(task_ids)
    for line in seq_outputs:
        print(line)
    print(f'Sequential Time: {seq_time:.2f} seconds\n')

    workers = 4
    print(f'Parallel Execution with ThreadPool ({workers} workers):')
    par_outputs, par_time = parallel_run(task_ids, workers=workers)
    for line in par_outputs:
        print(line)
    print(f'Parallel Time: {par_time:.2f} seconds')

    speedup = seq_time / par_time if par_time > 0 else 0
    print(f'Speedup: {speedup:.2f}x')


if __name__ == '__main__':
    main()
