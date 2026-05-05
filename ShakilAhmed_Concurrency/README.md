# Concurrency Assignment - Shakil Ahmed

## How to Run
- Part 1: `python part1_race_condition.py`
- Part 2: `python part2_producer_consumer.py`
- Part 3: `python part3_dining_philosophers.py`
- Part 4: `python part4_thread_pool.py`



## Part 1: Race Condition
This program shows a shared counter updated by 3 threads. Without a lock, updates overlap and the final value is usually wrong. With a lock, each increment becomes atomic and the final value is correct (3000).
I learned that unsynchronized shared data can produce race conditions and incorrect outputs.

## Part 2: Producer-Consumer
This program simulates bakers producing bread and customers consuming it using a bounded queue of size 5. The queue blocks producers when full and consumers when empty, which prevents overflow and underflow safely.
I learned that thread-safe queues simplify coordination between producer and consumer threads.

## Part 3: Dining Philosophers
This program runs 3 philosophers and 3 forks using locks. Deadlock is prevented by always picking the lower-numbered fork first, which removes circular waiting.
I learned that a small ordering rule can prevent deadlock in shared-resource systems.

## Part 4: Thread Pool
This program compares sequential execution with thread-pool execution for 10 tasks. The thread pool uses 4 worker threads and usually finishes faster due to parallel processing.
I learned that thread pools improve performance when tasks can run independently.
