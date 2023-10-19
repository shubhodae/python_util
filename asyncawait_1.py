import asyncio


async def get_data():
    print("getting data ....")
    await asyncio.sleep(8)
    print("data fetched ....")
    return {"data": 1}


async def print_data():
    print("starting to print data ...")
    for i in range(10):
        print(i)
        asyncio.sleep(1)
    print("printing data ended")


async def task():
    k = await get_data()
    print(k)


asyncio.run(task())