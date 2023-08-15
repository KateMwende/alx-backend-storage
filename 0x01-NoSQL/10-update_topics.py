#!/usr/bin/env python3
"""
changes all topics of a school document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """use name to change topics"""
    output = mongo_collection.update_many(
        {"name": name},
        {'$set': {'topics': topics}}
        )
