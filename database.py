# coding=utf8

import MySQLdb

def initdb():
    conn = MySQLdb.connect(host="localhost",user="root",passwd="root",db="amazing")
    cur = conn.cursor()
    tables = [(
	"drop table if exists books",

	"create table if not exists books ( "
	"number integer primary key not null, "
	"osis text not null, "
	"human text not null, "
	"chapters integer not null)"),

	(
	"drop table if exists chapters",

        "create table if not exists chapters ( "
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
        "index `next_osis_index` (`next_osis`,`next_osis_number`))"),

	(
	"drop table if exists verses",
	"create table if not exists verses (`id` integer primary key, book char(7), verse real, unformatted text)")
	]

    for (drop, create) in tables:
        cur.execute(drop)
        cur.execute(create)
    conn.commit()


if __name__ == '__main__':
    initdb()
