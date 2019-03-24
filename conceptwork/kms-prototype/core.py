#!/usr/bin/python3
import os
import sys
import sqlite3 as db
import argparse


class backend():
    def __init__(self):
        self.__filename = os.path.join(os.path.dirname(__file__), "dbase.clx")
        self.__connection = db.connect(self.__filename)

    def create_table(self):
        cursor = self.__connection.cursor()
        table_create_sql = """Create Table Resources (
            id integer PRIMARY KEY Autoincrement not null,
            title Text not null,
            file Text not null ,
            path Text not null ,
            tags Text not null
        )"""
        try:
            cursor.execute(table_create_sql)
        except:
            pass
        self.__connection.commit()

    def add_entry(self, **args):
        cursor = self.__connection.cursor()
        add_entry_sql = """INSERT into Resources (title,file,path,tags)
         values (?,?,?,?)"""
        cursor.execute(
            add_entry_sql, (args["title"], args["file"], args["path"], args["tags"]))
        self.__connection.commit()

    def get_all_data(self):
        cursor = self.__connection.cursor()
        query_sql = """select * from Resources"""
        cursor.execute(query_sql)
        return cursor.fetchall()

    def get_selected_item(self, key, value):
        cursor = self.__connection.cursor()
        query_sql = """select * from Resources where {0} = ?""".format(key)
        if type(value) != str:
            value = str(value)
        cursor.execute(query_sql, (value,))
        return cursor.fetchall()

    def update_item(self, id, key, value):
        update_sql = """update Resources 
        set {0}=? where id=?""".format(key)
        cursor = self.__connection.cursor()
        cursor.execute(update_sql, (value, str(id)))
        self.__connection.commit()

    def delete_item(self, id):
        delete_sql = """Delete from Resources where id =?"""
        cursor = self.__connection.cursor()
        cursor.execute(delete_sql, (str(id)))
        self.__connection.commit()

    def __getitem__(self, key):
        cursor = self.__connection.cursor()
        cursor.execute("select * from Resources")
        if type(key) == int:
            return self.get_selected_item("id", key)
        elif type(key) == str:
            return self.get_selected_item("title", key)
        else:
            raise TypeError("The argument must be id or title")


if __name__ == "__main__":
    pass
