"""Main app/routing file for Twitoff"""

from flask import Flask, render_template, request
import json
from .data_model import DB, User, Tweet
from .twitter import upsert_user
from .ml import predict_most_likely_author


def create_app():
    """Creating and configuring an instance of the Flask application"""
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    DB.init_app(app)

    @app.route('/')
    def index():
        DB.drop_all()
        DB.create_all()
        upsert_user("cher")
        upsert_user("elonmusk")
        upsert_user("barackobama")
        return render_template("base.html", title="Home")

    @app.route('/add_user', methods=['GET'])
    def add_user():
        twitter_handle = request.args['twitter_handle']
        upsert_user(twitter_handle)
        return 'insert successful'

    @app.route('/predict_author', methods=['GET'])
    def predict_author():
        tweet_to_classify = request.args['tweet_to_classify']
        return predict_most_likely_author(tweet_to_classify, ['cher', 'elonmusk', 'barackobama'])

    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return 'database_refreshed'

    return app

if __name__ == "__main__":
    create_app().run(host='0.0.0.0', port=8888)
