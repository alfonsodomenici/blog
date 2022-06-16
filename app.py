from flask import Flask, Response, request
from db_manager import mysql
from posts_resource import posts_resource
from flask_cors import CORS

import json

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

#db configuration
app.config['MYSQL_DATABASE_USER'] = 'blog'
app.config['MYSQL_DATABASE_PASSWORD'] = 'blog'
app.config['MYSQL_DATABASE_DB'] = 'db_post'
app.config['MYSQL_DATABASE_HOST'] = '192.168.12.209'

mysql.init_app(app)

app.register_blueprint(posts_resource)


@app.route('/')
def home():
    response = Response("Blog backend Works!!!")
    return response
