from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_cinnection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn
