/*
*Author:-Pukar Giri
*Created On:-26Th October 2018 at 10:51
*File Name:-sqlite.cpp
*Project Name:-templater
*Licence:- MIT
*Email:-crazzy.lx75@gmail.com
*/
#include <iostream>
#include "sqlitedb.h"



sqlitedb::sqlitedb(char *filename)
    {
        this->filename = filename;
    }



int sqlitedb::open()
    {
        int rc = sqlite3_open(this->filename, &db);
        if (rc)
        {
            std::cout << "Could not Connetct to database: " << sqlite3_errmsg(db);
        }
        return rc;
    }



int sqlitedb::close()
    {
        sqlite3_close(db);
    }



int sqlitedb::execute(const char *command, sqlite3_callback callback, void *data)
    {
        char *zerrmsg = 0;
        this->open();
        int rc = sqlite3_exec(db, command, callback, data, &zerrmsg);
        if (rc != SQLITE_OK)
        {
            std::cout << "Execution of the command failed : " << zerrmsg << std::endl;
        }
        this->close();
    }



void sqlitedb::new_entry(std::string alias, std::string filename, std::string path)
    {
        std::string sql = "INSERT into paths (alias, filename, path) values('" + alias + "','" + filename + "','" +
                          path + "')";
        this->execute(sql.c_str(), nullptr, nullptr);
    }



void sqlitedb::search_for(std::string alias, sqlite3_callback callback, void *data)
    {
        std::string sql = "SELECT path FROM paths WHERE alias == '" + alias + "'";
        this->execute(sql.c_str(), callback, data);
    }
