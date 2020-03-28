"""Decorators collection"""

from time import time


def example_dec(func):
    """Prints the doc of a function"""
    def inner(*args, **kwargs):
        print(func.__doc__)
        return func(*args, **kwargs)
    return inner


def timeit_dec(func):
    """Decorator for measure the execution time of a function"""
    def inner(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f'Excution time {func.__name__}: {end - start}')
        return result
    return inner
