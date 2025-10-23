from abc import ABC, abstractmethod
from typing import List
from pymongo import MongoClient
from pymongo.errors import PyMongoError

from ..config import MONGO, DATABASE, COLLECTION
from ..models.task import Task

class TaskRepository(ABC):
    @abstractmethod
    async def list(self) -> List[Task]:
        pass

    @abstractmethod
    async def read(self, id: str) -> Task:
        pass

    @abstractmethod
    async def create(self, task: Task) -> Task:
        pass

    @abstractmethod
    async def update(self, id: str, task: Task) -> Task:
        pass

    @abstractmethod
    async def delete(self, id: str) -> None:
        pass

class MongoDBTaskRepository(TaskRepository):
    def __init__(self, uri: str = MONGO):
        self.client = MongoClient(uri)
        self.db = self.client[DATABASE]
        self.collection = self.db[COLLECTION]

    async def list(self) -> List[Task]:
        try:
            tasks = self.collection.find()
            return [Task(**task) for task in tasks]
        except PyMongoError as e:
            raise Exception(f"Error listing tasks: {e}")
        
    async def read(self, id: str) -> Task:
        try:
            task = self.collection.find_one({"_id": id})
            if task is None:
                raise Exception(f"Task not found with id: {id}")
            return Task(**task)
        except PyMongoError as e:
            raise Exception(f"Error reading task: {e}")
    
    async def create(self, task: Task) -> Task:
        try:
            result = self.collection.insert_one(task.dict())
            task.id = str(result.inserted_id)
            return task
        except PyMongoError as e:
            raise Exception(f"Error creating task: {e}")
        
    async def update(self, id: str, task: Task) -> Task:
        try:
            result = self.collection.update_one({"_id": id}, {"$set": task.dict()})
            if result.matched_count == 0:
                raise Exception(f"Task not found with id: {id}")
            return task
        except PyMongoError as e:
            raise Exception(f"Error updating task: {e}")
        
    async def delete(self, id: str) -> None:
        try:
            result = self.collection.delete_one({"_id": id})
            if result.deleted_count == 0:
                raise Exception(f"Task not found with id: {id}")
        except PyMongoError as e:
            raise Exception(f"Error deleting task: {e}")
        
    def __del__(self):
        self.client.close()