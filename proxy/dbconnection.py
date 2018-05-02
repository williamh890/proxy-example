from proxy import Proxy
from connection import Connection



class DBConnection(Proxy):
    def __init__(self, commands=[]):
        print("Made db connection objection")
        self.commands = commands

    def get(self):
        print("making connection to db...\n")
        return self.make_db_connection()

    def make_db_connection(self):
        return Connection()

    def add(self, query):
        self.commands.append(query)

    def commit(self):
        connection = self.get()
        if not connection:
            raise Exception("Cannot connect to database...")

        for query in self.commands:
            print(f"    making query to db -> {query}")

        connection.close()
