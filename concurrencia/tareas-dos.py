import asyncio


async def myCoroutine(param, dt):
    print("My Coroutine", param)
    await asyncio.sleep(dt)
    print("dos", param)


async def main():
    current = asyncio.Task.current_task()
    print(current)
    await asyncio.sleep(10)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.create_task(myCoroutine("a", 7))
        loop.create_task(myCoroutine("b", 5))
        loop.create_task(myCoroutine("c", 3))
        loop.run_until_complete(main())
        print("fin")
    finally:
        loop.close()
