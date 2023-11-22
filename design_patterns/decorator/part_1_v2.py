import time
from typing import Callable, Any, TypeVar

T = TypeVar("T")


def time_it(func: Callable[[Any], T]) -> Callable[[Any], T]:
    def wrapper(*args, **kwargs) -> T:
        start_time = time.perf_counter_ns()
        result = func(*args, **kwargs)
        end_time = time.perf_counter_ns()
        print(f"{func.__name__} took {end_time - start_time} ns")
        return result

    return wrapper


@time_it
def some_op() -> int:
    print("Start some op")
    time.sleep(1)
    print("We are done")
    return 123


if __name__ == "__main__":
    some_op()
