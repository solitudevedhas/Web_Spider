#!/usr/bin/env python

from pymongo import Connection

from searchengine.logger import Logging
from searchengine.settings import MONGO_HOST, MONGO_PORT, MONGO_NAME

class MongoDB(object):
    """
    A simple MongoDB wrapper which establishes a connection to a specified host
    and port, adds, update and delete data and query the database.
    """
    def __init__(self, collection_name, *args, **kwargs):
        self.log = kwargs.get('log', Logging())
        self.host = kwargs.get('host', MONGO_HOST)
        self.port = kwargs.get('port', MONGO_PORT)
        self.database_name = kwargs.get('database_name', MONGO_NAME)
        self.connection = kwargs.get('connection', Connection(host=self.host, port=self.port))
        self.database = self.connection[self.database_name]
        self.collection = self.database[collection_name]
        self.unique_indexes = kwargs.get("unique_indexes", [])
        
        # create all required indexes
        for index in self.unique_indexes:
            if self.collection.ensure_index(index, unique=True):
                self.log.info("MongoDB", "insert", "New db index created: %s" % index)
        
    def insert(self, data):
        """
        Add a data dict and indexes to the specified database.
        """
        return self.collection.insert(data)
        
    def update(self, data, id_obj=None, query_data=None):
        """
        Edit a data entry using the id or query_data as a unique identifier.
        """
        if id_obj:
            return self.collection.update({'_id': id_obj}, {"$set": data})
        return self.collection.update(query_data, {"$set": data})
        
    def remove(self, id_obj=None, query_data=None):
        """
        Remove a data entry using the id or query_data as a unique identifier.
        """
        if id_obj:
            return self.collection.remove(id_obj, query_data)
        return self.collection.remove(query_data)
        
    def find(self, query_data=None):
        """
        Return a list of entries matching the query data or all entries if not
        specified.
        """
        if query_data:
            return self.collection.find(query_data)
        return self.collection.find()
        
    def get(self, query_data=None, id_obj=None):
        """
        Get a single entry specified by either the id or the given query data.
        """
        if id_obj:
            return self.collection.find_one({'_id': id_obj})
        return self.collection.find_one(query_data)
