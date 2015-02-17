# coding=utf8

from models import Entry
from flask import Blueprint, render_template


index_page = Blueprint('index_page', __name__, template_folder='templates')

@index_page.route('/')
def index():
    entries = Entry.gets_all()
    return render_template('index.html', entries=entries)


