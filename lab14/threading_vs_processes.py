import time
import threading
import multiprocessing



def task():
    global x
    x=x+1
    # print(f'x in {threading.current_thread().name}')
    time.sleep(1)


def threading_demo():
    threads = []
    for _ in range(10):
        # task(1)
        tr = threading.Thread(target=task)
        threads.append(tr)
        tr.start()

    for tr in threads:
        tr.join()

def multiprocessing_demo():
    processes = []
    for _ in range(10):
        # task(1)
        pr = multiprocessing.Process(target=task)
        processes.append(pr)
        pr.start( )

    for pr in processes:
        pr.join()



if __name__ == '__main__':
    x = 1
    # start = time.time()
    # threading_demo()
    # end = time.time()
    # print(f'x={x}')
    # print(f'Time taken for threading_demo: {end-start}')

    start = time.time()
    multiprocessing_demo()
    end = time.time()
    print(f'x={x}')
    print(f'Time taken for multiprocessing_demo: {end-start}')