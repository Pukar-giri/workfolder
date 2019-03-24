/*
*Author:-Pukar Giri
*Created On:-26Th October 2018 at 09:11
*File Name:-main.cpp
*Project Name:-templater
*Licence:- MIT
*Email:-crazzy.lx75@gmail.com
*/

#include <iostream>
#include "sqlitedb.h"

static int return_handler(void *data, int argc, char **argv, char **azColname);

int main(int argc,char * argv))
    {
        void * data= nullptr;
        sqlitedb database("database.db");
        database.search_for("words",return_handler,data);
        return 0;
    }



static int return_handler(void *data, int argc, char **argv, char **azColname)
    {
        if (argc <= 0)
        {
            std::cout<<"sorry the data must be corupted";
            return -1;
        }
        else{
            std::cout<<argv[0]<<std::endl;
            return 0;
        }
    }
