import time
import threading

# IO bound
def task(x):
    print('START')
    print(x)
    time.sleep(1)
    print('END')


def main():
    threads = []
    for _ in range(3):
        tr = threading.Thread(target=task, args=(1,))
        # task(1)
        threads.append(tr)
        tr.start()

    for tr in threads:
        tr.join()



if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f'Time taken: {end-start}')