import asyncio


async def myTask(n):
    await asyncio.sleep(1)
    print("Processing {}".format(n))


async def myGenerator():
    for i in range(5):
        asyncio.ensure_future(myTask(i))
    print("Completed Tasks")
    await asyncio.sleep(2)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(myGenerator())
        print('fin')
    finally:
        loop.close()
