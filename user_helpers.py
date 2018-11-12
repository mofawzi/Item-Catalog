#!/usr/bin/env python2.7

from flask import session as login_session

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import User


DBSession = sessionmaker(bind=engine)
session = DBSession()


# User Helper Functions

def createUser(login_session):
    """ This method creates a new user
     and save its information to the database """
     
    newUser = User(name=login_session['username'], email=login_session[
                   'email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    if user:
        return user
    else:
        return None


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None