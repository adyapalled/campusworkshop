"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaajdik728r886nlvdg-a.oregon-postgres.render.com",
        database="todo_58ax",
        user="todo_58ax_user",
        password="T9LSEGNW3g3mvDyRB8mPUv44Cwpf7LnX")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
