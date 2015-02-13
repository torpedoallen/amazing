CREATE TABLE books (number INTEGER PRIMARY KEY NOT NULL, osis TEXT NOT NULL, human TEXT NOT NULL, chapters INTEGER NOT NULL);
CREATE TABLE chapters (reference_osis VARCHAR PRIMARY KEY NOT NULL, reference_human VARCHAR NOT NULL, content TEXT NOT NULL, previous_reference_osis VARCHAR, previous_reference_human VARCHAR, next_reference_osis VARCHAR, next_reference_human VARCHAR);
CREATE TABLE verses (id INTEGER PRIMARY KEY, book CHAR(7), verse REAL, unformatted TEXT);
CREATE TABLE metadata (name TEXT PRIMARY KEY NOT NULL, value TEXT);
CREATE TABLE annotations (id INTEGER PRIMARY KEY, osis VARCHAR NOT NULL, link VARCHAR NOT NULL, content TEXT NOT NULL, UNIQUE (osis, link));
CREATE INDEX verse_lookup_index on verses (book, verse);
CREATE INDEX annotation_lookup_index on annotations (osis);
