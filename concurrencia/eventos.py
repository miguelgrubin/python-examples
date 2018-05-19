import asyncio


async def hello_world():
    await asyncio.sleep(1)
    print('Hello World')
    await hello_world()


async def good_evening():
    await asyncio.sleep(1)
    print('Good Evening')
    await good_evening()


def main():
    print('step: asyncio.get_event_loop()')
    loop = asyncio.get_event_loop()
    try:
        print('step: loop.run_until_complete()')
        asyncio.async(hello_world())
        asyncio.async(good_evening())
        loop.run_forever()
    finally:
        print('step: loop.close()')
        loop.close()


if __name__ == '__main__':
    main()
