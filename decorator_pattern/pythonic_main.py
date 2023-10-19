import logging
from abc import ABC, abstractmethod
from math import sqrt
from time import perf_counter
from typing import Callable, Any
import functools

logger = logging.getLogger("my_app")


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for element in range(2, int(sqrt(number)) + 1):
        if number % element == 0:
            return False
    return True


def benchmark(func: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = perf_counter()
        value = func(*args, **kwargs)
        end_time = perf_counter()
        run_time = end_time - start_time
        logging.info(
            f"Execution of {func.__name__} took {run_time:.2f} seconds"
        )  # fmt: skip
        return value

    return wrapper


def with_logging(logger: logging.Logger):
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            logger.info(f"Calling {func.__name__}")
            value = func(*args, **kwargs)
            logging.info(f"Finished calling {func.__name__}")
            return value

        return wrapper

    return decorator


@with_logging(logger)
@benchmark
def count_prime_numbers(upper_bound: int) -> int:
    count = 0
    for number in range(upper_bound):
        if is_prime(number):
            count += 1
    return count


# class LoggingDecorator(AbstructDecorator):
#     def execute(self, upper_bound: int) -> int:
#         logging.info(f"Calling {self._decorated.__class__.__name__}")
#         value = self._decorated.execute(upper_bound)
#         logging.info(f"Finished calling {self._decorated.__class__.__name__}")
#         return value


def main() -> None:
    logging.basicConfig(level=logging.INFO)
    value = count_prime_numbers(100000)
    logging.info(f"Number of primes: {value}.")


if __name__ == "__main__":
    main()
