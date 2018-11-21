#!/usr/bin/env python2.7

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import session as login_session
from database_setup import Base, User


engine = create_engine(
    'sqlite:///restaurantmenuwithusers.db?check_same_thread=False')
Base.metadata.bind = engine

# Create the database session to apply CRUD
DBSession = sessionmaker(bind=engine)
session = DBSession()


# User Helper Functions
def createUser(login_session):
    """ This method creates a new user taking its info from the
        login session and save it to the database """

    newUser = User(name=login_session['username'], email=login_session[
                   'email'], picture=login_session['picture'])

    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(
        email=login_session['email']).one()

    return user.id


def getUserInfo(user_id):
    """ This method gets the info of a user """

    user = session.query(User).filter_by(
        id=user_id).one()

    return user


def getUserID(email):
    """ This method returns the user's Id """

    try:
        user = session.query(User).filter_by(
            email=email).one()

        return user.id
    except Exception:
        return None
