# coding=utf8



from flask import g


class Entry(object):


    def __init__(self, number, osis, human, chapters):
        self.number = number
        self.osis = osis
        self.human = human
        self.chapters = chapters

    @classmethod
    def gets_all(cls):
        cur = g.db.cursor()
        ret = cur.execute('select number, osis, human, chapters from books')
        return [cls(*t) for t in ret]

    @property
    def url(self):
        return '/entry/%s' % self.number
