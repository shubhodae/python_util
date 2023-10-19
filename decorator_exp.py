import logging
from time import perf_counter
from functools import wraps
from typing import Callable, Any


def logging_decorator(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: any, **kwargs: any) -> any:
        start_time = perf_counter()
        logging.info(f"Start calling: {start_time}")
        value = func(*args, **kwargs)
        end_time = perf_counter()
        logging.info(f"end execution: {end_time}")
        total_time = end_time - start_time
        logging.info(f"Total time: {total_time}")
        return value

    return wrapper


@logging_decorator
def test_func(i: int) -> None:
    for i in range(i):
        print(i)


def main() -> None:
    logging.basicConfig(level=logging.INFO)
    test_func(20)


if __name__ == "__main__":
    main()
