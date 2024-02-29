import asyncio

async def async_func(task_no):
    """ Asynchronous function to simulate a task, taking 1 second """
    print(f'{task_no} is started ...')
    await asyncio.sleep(1)
    print(f'{task_no} ends!')

async def main():
    """  Main asynchronous function to run multiple tasks concurrently. """
    taskA = asyncio.create_task(async_func('taskA'))
    taskB = asyncio.create_task(async_func('taskB'))
    taskC = asyncio.create_task(async_func('taskC'))
    await asyncio.wait([taskA, taskB, taskC])

if __name__ == "__main__":

    asyncio.run(main()) # start event loop
