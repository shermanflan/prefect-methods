from prefect import flow, task
from prefect.futures import wait
from prefect.task_runners import ThreadPoolTaskRunner, ProcessPoolTaskRunner
import time

"""
ThreadPoolTaskRunner uses Python Threads which run in a single process
and provide an illusion of parallelism. By contrast, ProcessPoolTaskRunner
uses processes (Python multiprocessing) and achieves true parallelism.
"""
@task
def stop_at_floor(floor):
    print(f"elevator moving to floor {floor}")
    time.sleep(floor)
    print(f"elevator stops on floor {floor}")

@flow(task_runner=ThreadPoolTaskRunner(max_workers=3))
# @flow(task_runner=ProcessPoolTaskRunner(max_workers=3))
def elevator():
    floors = []

    for floor in range(10, 0, -1):
        floors.append(stop_at_floor.submit(floor))

    wait(floors) # wait for the sequence of futures to complete


if __name__ == "__main__":
    elevator()