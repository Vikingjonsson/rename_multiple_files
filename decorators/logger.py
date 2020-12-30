from typing import Callable
import functools


def log(_func: Callable = None, *, type: str = '') -> Callable:
    def decorator_logger(func) -> Callable:
        @functools.wraps(func)
        def wrapper_logger(*args, **kwargs) -> str:
            if type == 'debug':
                print(
                    f'{type.upper()}: calling "{func.__name__}" with {args} and {kwargs}')
            return func(*args, **kwargs)
        return wrapper_logger

    if _func is None:
        return decorator_logger
    else:
        return decorator_logger(_func)
