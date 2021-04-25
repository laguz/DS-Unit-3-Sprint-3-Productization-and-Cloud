"""Main app/routing file for Twitoff"""

from flask import Flask, render_template, request
import json
from .data_model import DB, User, Tweet
from .twitter import upsert_user


def create_app():
    """Creating and configuring an instance of the Flask application"""
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    DB.init_app(app)

    @app.route('/')
    def landing():
        DB.drop_all()
        DB.create_all()
        app_user = User(id=1,name='app_user')
        DB.session.add(app_user)
        DB.session.commit()
        upsert_user("elonmusk")
        with open('/Users/laguz/Documents/DS-Unit-3-Sprint-3-Module1/twitoff/templates/landing.json') as f:
            args = json.load(f)
        return render_template("base.html", **args)

    @app.route('/add_user', methods=['GET'])
    def add_user():
        twitter_handle = request.args['twitter_handle']
        upsert_user(twitter_handle)
        return 'insert success'

    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return 'database_refreshed'

    return app

if __name__ == "__main__":
    create_app().run(host='0.0.0.0', port=8888)
