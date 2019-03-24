/*
*Author:-Pukar Giri
*Created On:-26Th October 2018 at 10:51
*File Name:-sqlite.h
*Project Name:-templater
*Licence:- MIT
*Email:-crazzy.lx75@gmail.com
*/

#ifndef TEMPLATER_SQLITE_H
#define TEMPLATER_SQLITE_H

#include <sqlite3.h>
#include <iostream>

class sqlitedb
    {
    public:
        explicit sqlitedb(char* filename);
        int execute(const char *command,sqlite3_callback callback, void*data);
        void new_entry(std::string alias ,std::string filename,std::string path);
        void search_for(std::string alias,sqlite3_callback callback, void* data);
    private:
        int open();
        int close();
        char* filename;
        sqlite3 *db;

    };



#endif //TEMPLATER_SQLITE_H
