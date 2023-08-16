#!/usr/bin/env python3
"""
Module that creates redis classes and methods
"""
from functools import wraps
import redis
import uuid
from typing import Union, Callable


def count_calls(method: Callable) -> Callable:
    """Counts times cache is called"""
    key = method.__qualname__
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrap deco function and return wrapper"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

class Cache:
    """creates class cache with instance of Redis client"""
    def __init__(self):
        """initializes _redit and fushes database"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generate a random key and stores it in Redis"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Callable = None
            ) -> Union[str, bytes, int, float]:
        """convert the data back to the desired format"""
        value = self._redis.get(key)
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        """Return a string"""
        value = self._redis.get(key)
        return value.decode("utf-8")

    def get_int(self, key: int) -> int:
        """Return an int"""
        value = self._redis.get(key)
        return int(value.decode("utf-8"))
