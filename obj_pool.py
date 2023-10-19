from abc import ABC, abstractmethod


class MongodbConnction:
    def get_db(self):
        return f"[[ mongodb connection ]] :: {id(self)}"


class PoolInterface(ABC):
    @abstractmethod
    def acquire(self):
        pass

    @abstractmethod
    def release(self, obj):
        pass


class MongoDBConnctionPool(PoolInterface):
    def __init__(self, size) -> None:
        self.size = size
        self.free_to_use = list()
        self.in_use = list()

        for _ in range(self.size):
            self.free_to_use.append(MongodbConnction())

    def acquire(self) -> MongodbConnction:
        if len(self.free_to_use) <= 0:
            raise Exception("No more connction available")
        r = self.free_to_use[0]
        self.in_use.append(r)
        self.free_to_use.remove(r)
        return r

    def release(self, obj: MongodbConnction):
        self.in_use.remove(obj)
        self.free_to_use.append(obj)


class MongoDBConnctionPoolManager:
    def __init__(self, pool: MongoDBConnctionPool) -> None:
        self.pool = pool

    def __enter__(self):
        self.r = self.pool.acquire()
        return self.r

    def __exit__(self, type, value, traceback):
        self.pool.release(self.r)


if __name__ == "__main__":
    print("Hello !!")

    pool = MongoDBConnctionPool(1)

    with MongoDBConnctionPoolManager(pool) as r:
        connction = r.get_db()
        print(connction)

    with MongoDBConnctionPoolManager(pool) as r:
        connction = r.get_db()
        print(connction)

    with MongoDBConnctionPoolManager(pool) as r:
        connction = r.get_db()
        print(connction)

    with MongoDBConnctionPoolManager(pool) as r:
        connction = r.get_db()
        print(connction)

    with MongoDBConnctionPoolManager(pool) as r:
        connction = r.get_db()
        print(connction)
