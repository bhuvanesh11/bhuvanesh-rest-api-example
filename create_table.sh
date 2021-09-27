#!/bin/sh

sqlite3 example.db "CREATE TABLE User( \
		ids INTEGER PRIMARY KEY, \
		name VARCHAR NOT NULL UNIQUE, \
		email VARCHAR type NOT NULL UNIQUE, \
		password VARCHAR, \
		lastlogintime TEXT);"
