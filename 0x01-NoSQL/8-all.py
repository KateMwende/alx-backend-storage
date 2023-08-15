#!/usr/bin/env python3
"""
lists all documents in a collection
"""


def list_all(mongo_collection):
    """lists all documents"""
    documents = []

    cursor = mongo_collection.find()

    for document in cursor:
        documents.append(document)
    return documents
