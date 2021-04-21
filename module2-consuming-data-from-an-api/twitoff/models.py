"""SQLAlchemy models and utility functions for Twioff Application"""

from flask_sqlalchemy import SQLAlchemy
#from .twitter import add_or_update_user


DB = SQLAlchemy()


# User Table
class User(DB.Model):
    """Twitter User Table that will correspond to tweets - SQLAlchemy syntax"""
    id = DB.Column(DB.BigInteger, primary_key=True) # id column (primary key)
    name = DB.Column(DB.String, nullable=False) # name column
    # keeps track of recent user tweets
    newest_tweet_id = DB.Column(DB.BigInteger)

    def __repr__(self):
        return "<User: {}>".format(self.name)


# Twitter Table
class Tweet(DB.Model):
    """Tweet text data - associated with Users Table"""
    id = DB.Column(DB.BigInteger, primary_key=True) # id column (primary key)
    text = DB.Column(DB.Unicode(300))
    vect = DB.Column(DB.PickleType, nullable=False)
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey("user.id"), nullable=False)
    user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))

    def __repr__(self):
        return "<Tweet: {}>".format(self.text)

from .twitter import add_or_update_user
def insert_example_users():
    """We will get an error if we run this twice witho droping & creating"""
    add_or_update_user("elonmusk")


    """nick = User(id=1, name="nick")
    elon = User(id=1, name="elonmusk")
    DB.session.add(nick)
    DB.session.add(elon)
    DB.session.commit()"""
