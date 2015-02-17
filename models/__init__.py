# coding=utf8



from database import mysql_conn, sqlite_db


class Entry(object):


    def __init__(self, number, osis, human, chapters):
        self.number = number
        self.osis = osis
        self.human = human
        self.chapters = chapters

    @classmethod
    def gets_all(cls):
        cur = sqlite_db.cursor()
        ret = cur.execute('select number, osis, human, chapters from books')
        return [cls(*t) for t in ret]

    @property
    def url(self):
        return '/entry/%s' % self.number

class OldChapter(object):


    def __init__(self, reference_osis, reference_human, content, previous_reference_osis, previous_reference_human, next_reference_osis, next_reference_human):
        self.reference_osis = reference_osis
        self.reference_human = reference_human
        self.content = content
        self.previous_reference_osis = previous_reference_osis
        self.previous_reference_human = previous_reference_human
        self.next_reference_osis = next_reference_osis
        self.next_reference_human =  next_reference_human

    @classmethod
    def gets_all(cls):
        cur = sqlite_db.cursor()
        ret = cur.execute('select reference_osis, reference_human, content, previous_reference_osis, previous_reference_human, next_reference_osis, next_reference_human from chapters')
        return [cls(*t) for t in ret]

class Chapter(object):


    def __init__(self, osis_number, osis, human, content, previous_osis, previous_human,
            previous_osis_number, next_osis, next_osis_number, next_human):
        self.osis_number = osis_number
        self.osis = osis
        self.human = human
        self.content = content
        self.previous_osis = previous_osis
        self.previous_osis_number = previous_osis_number
        self.previous_human = previous_human
        self.next_osis = next_osis
        self.next_osis_number = next_osis_number
        self.next_human = next_human

    @classmethod
    def add(cls):
        ret = mysql_conn.cursor().execute('insert into chapters')


if __name__ == "__main__":
    OldChapter.gets_all()
