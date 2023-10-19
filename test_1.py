import asyncio

async def fetch_data():
    print('starting to feth data ---------')
    await asyncio.sleep(5)
    print('fetch data ended ------------')
    return {
        "data": 1
    }

async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(1)


async def test_run():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())

    value = await task1
    print(value)
    await task2
    value['data'] = 99
    return value

def main():
    k = asyncio.run(test_run())
    print(k)


main()