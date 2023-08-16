#!/usr/bin/env python3
"""
Module that creates redis classes and methods
"""
import redis
import uuid
from typing import Union


class Cache:
    """creates class cache with instance of Redis client"""
    def __init__(self):
        """initializes _redit and fushes database"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generate a random key and stores it in Redis"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
