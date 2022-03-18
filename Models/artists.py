import sqlite3

class Artist:

    def __init__(self, cursor: sqlite3.Cursor, id: int, name: str):
        self.__cursor = cursor       
        self.ArtistId = id
        self.Name = name

    def ToDict(self):
        return self.__dict__

    def SendToDb(self):
        sql = f"INSERT INTO artists (Name) VALUES (\'{self.Name}\')"
        self.__cursor.execute(sql)