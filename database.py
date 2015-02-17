# coding=utf8

import sqlite3
import MySQLdb

SQLITE_DATABASE_URI = 'bible.db'
sqlite_db = sqlite3.connect(SQLITE_DATABASE_URI)
mysql_conn = MySQLdb.connect(host="localhost",user="root",passwd="root", db="amazing")

def initdb():
    conn = mysql_conn
    cur = conn.cursor()
    tables = [(
	"drop table if exists books",

	"create table books ( "
	"number integer not null, "
	"osis text not null, "
	"human text not null, "
	"chapters integer not null, "
        "primary key (`number`) "
	")"),

	(
	"drop table if exists chapters",

        "create table chapters ( "
        "osis varchar(10) not null, "
        "osis_number int(3) not null, "
        "human varchar(20) not null, "
        "content text not null, "
        "previous_osis varchar(10), "
        "previous_osis_number int(3) default null, "
        "previous_human varchar(20), "
        "next_osis varchar(10), "
        "next_osis_number int(3) default null, "
        "next_human varchar(20), "
        "primary key (`osis`,`osis_number`), "
        "index `previous_osis_index` (`previous_osis`,`previous_osis_number`), "
        "index `next_osis_index` (`next_osis`,`next_osis_number`)"
	")"),

	(
	"drop table if exists verses",

	"create table verses ("
	"`id` integer not null, "
	"book char(7), "
	"verse real, "
	"unformatted text, "
        "primary key (`id`), "
	"index `verse_lookup_index` (`book`, `verse`)"
	")"),

	(
	"drop table if exists metadata",

	"create table metadata ("
	"`name` varchar(64) not null, "
	"value varchar(128), "
        "primary key (`name`) "
	")"),

	(
	"drop table if exists annotations",

	"create table annotations ("
	"`id` integer not null, "
	"osis varchar(10) not null, "
	"`link` varchar(64) not null, "
	"content text not null, "
        "primary key (`id`), "
	"unique key `annotation_unique_key` (`osis`, `link`)"
	")"),
	]

    for (drop, create) in tables:
        cur.execute(drop)
        cur.execute(create)
    conn.commit()




if __name__ == '__main__':
    initdb()
