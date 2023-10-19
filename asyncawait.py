import asyncio


async def get_data():
    print("fetching data start ....")
    await asyncio.sleep(4)
    print("fetching data ended ....")
    return {
        "data": 1
    }  # fmt: skip


async def print_data():
    print("starting to print")
    for i in range(10):
        print(i)
        await asyncio.sleep(1)
    print("printing ended ...")


async def tasks():
    task1 = asyncio.create_task(get_data())
    task2 = asyncio.create_task(print_data())

    value = await task1
    print(value)
    await task2
    return {
        "message": "response message"
    }  # fmt: skip


def main():
    r = asyncio.run(tasks())
    print(r)


main()
