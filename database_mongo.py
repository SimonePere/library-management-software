# database_mongo.py
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure




class DatabaseMongo:
    def __init__(self, host="localhost", port=27017, db_name="libreria_mele"):
        self.host = host
        self.port = port
        self.db_name = db_name
        self.client = None
        self.db = None

    def connetti(self):
        try:
            self.client = MongoClient(self.host, self.port)
            self.db = self.client[self.db_name]
            server_info = self.client.server_info()
            print(f"Connesso a Mongodb: {server_info["version"]}")
        except ConnectionFailure as e:
            print(f"Errore di connessione {e}")

    def disconnetti(self):
        if self.client:
            self.client.close()
            print("Disconnesso da MongoDB")
