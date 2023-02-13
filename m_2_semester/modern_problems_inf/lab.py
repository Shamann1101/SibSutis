import threading
from abc import ABC
from datetime import datetime
from time import sleep
from random import randint

global_lock = threading.Lock()


class Worker(ABC):
    def __init__(self, filename: str, priority: int = 1):
        if priority < 1:
            raise ValueError('Priority must be positive')
        self.filename = filename
        self.priority = priority
        self.thread = threading.Thread(target=self.action)

    def __str__(self):
        return f'Thread[{threading.get_ident()}]'

    def action(self):
        pass


class Reader(Worker):
    def action(self):
        self._read()

    def _read(self):
        with open(self.filename, 'r') as file:
            symbol = file.read(1)
            print(f'{self}: {symbol}')


class Writer(Worker):
    def action(self):
        self._write()

    def _write(self):
        # while global_lock.locked():
        #     sleep(0.01)
        #     continue
        #
        # global_lock.acquire()

        with global_lock:
            with open(self.filename, 'a+') as file:
                file.write(str(randint(0, 10)))
                # file.write("\n")
                file.close()

        # global_lock.release()


def _get_rnd_worker(workers: list) -> Worker:
    worker_list = []
    for worker in workers:
        worker_list += [worker] * worker.priority

    return worker_list[randint(0, len(worker_list) - 1)]


def write_to_file():
    # while global_lock.locked():
    #     sleep(0.01)
    #     continue
    #
    # global_lock.acquire()

    with global_lock:
        with open("thread_writes.txt", "a+") as file:
            file.write(str(threading.get_ident()))
            file.write("\n")
            file.close()

    # global_lock.release()


def _main():
    # Create a 200 threads, invoke write_to_file() through each of them,
    # and
    threads = []
    st = datetime.now()

    for i in range(1, 201):
        print(i)
        t = threading.Thread(target=write_to_file)
        threads.append(t)
        t.start()
    [thread.join() for thread in threads]

    nd = datetime.now()
    print("Ex time: ", (nd - st).total_seconds())


def _mainn():
    workers = []

    data_file = __file__.split('.')[0] + '_data.txt'

    writers = []
    writers.append(Writer(data_file))

    readers = []
    for i in range(5):
        readers.append(Reader(data_file, i + 1))

    workers.extend(writers)
    workers.extend(readers)

    # [worker.thread.start() for worker in workers]

    for _ in range(100):
        worker = _get_rnd_worker(workers)
        print(f'{worker} in work')
        # if worker.__class__ == Worker:
        #     [worker.thread.join() for worker in readers]
        #     worker.thread.run()
        #     # [worker.thread.start() for worker in readers]
        # else:
        #     worker.thread.run()
        worker.thread.start()
    [worker.thread.join() for worker in workers]


if __name__ == '__main__':
    _mainn()
