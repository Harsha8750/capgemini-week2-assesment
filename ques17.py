from abc import ABC, abstractmethod

class IDatabaseOperations(ABC):
    @abstractmethod
    def insert(self, data):
        pass

    @abstractmethod
    def update(self, data):
        pass

    @abstractmethod
    def delete(self, data):
        pass

class SQLDatabase(IDatabaseOperations):
    def insert(self, data):
        print(f"Inserting {data} into SQL database")

    def update(self, data):
        print(f"Updating {data} in SQL database")

    def delete(self, data):
        print(f"Deleting {data} from SQL database")

class NoSQLDatabase(IDatabaseOperations):
    def insert(self, data):
        print(f"Inserting {data} into NoSQL database")

    def update(self, data):
        print(f"Updating {data} in NoSQL database")

    def delete(self, data):
        print(f"Deleting {data} from NoSQL database")


sql_db = SQLDatabase()
nosql_db = NoSQLDatabase()

sql_db.insert("record1")
sql_db.update("record1")
sql_db.delete("record1")

nosql_db.insert("document1")
nosql_db.update("document1")
nosql_db.delete("document1")
