#!/usr/bin/env python2.7


from flask import Flask, render_template, request, redirect, url_for
from flask import flash


# Database imports
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

# Use the Flask framework
app = Flask(__name__)

# Create the database engine
engine = create_engine('sqlite:///restaurantsmenu.db?check_same_thread=False')
Base.metadata.bind = engine

# Create the database session to apply CRUD
DBSession = sessionmaker(bind=engine)
session = DBSession()


# Get all restaurants route
@app.route('/', methods=['GET'])
@app.route('/restaurants')
def showRestaurants():
    """This method should retrieve all restaurants
    from the database and show them to the users"""

    restaurants = session.query(Restaurant)
    return render_template('restaurants.html', restaurants=restaurants)


# Create restaurant route
@app.route(
    '/restaurant/new',
    methods=['GET', 'POST'])
def newRestaurant():
    """This method should Create a new restaurant
    and save it to the database"""

    if request.method == 'POST':
        newRestaurant = Restaurant(
            name=request.form['name'])

        session.add(newRestaurant)
        session.commit()
        flash('Restaurant " %s " is Successfully Created!' % newRestaurant.name)
        return redirect(url_for('showRestaurants'))
    else:
        return render_template('newRestaurant.html')


# Edit restaurant route
@app.route(
    '/restaurant/<int:restaurant_id>/edit',
    methods=['GET', 'POST'])
def editRestaurant(restaurant_id):
    """This method should Update or Edit a restaurant
    and save the changes to the database"""

    editedRestaurant = session.query(Restaurant).filter_by(
        id=restaurant_id).one()

    if request.method == 'POST':
        if request.form['name']:
            editedRestaurant.name = request.form['name']
        session.add(editedRestaurant)
        session.commit()
        flash('Restaurant " %s " is Successfully Edited!' % editedRestaurant.name)
        return redirect(url_for('showRestaurants'))
    else:
        return render_template(
            'editRestaurant.html', restaurant=editedRestaurant)


# Delete restaurant route
@app.route(
    '/restaurant/<int:restaurant_id>/delete',
    methods=['GET', 'POST', 'Delete'])
def deleteRestaurant(restaurant_id):
    """This method should Delete a restaurant from the database"""

    deletedRestaurant = session.query(Restaurant).filter_by(
        id=restaurant_id).one()

    if request.method == 'POST':
        session.delete(deletedRestaurant)
        session.commit()
        flash('Restaurant " %s " is Successfully Deleted!' % deletedRestaurant.name)
        return redirect(url_for('showRestaurants'))
    else:
        return render_template(
            'deleteRestaurant.html', restaurant=deletedRestaurant)


# Show the menu of a restaurant route
@app.route(
    '/restaurant/<int:restaurant_id>/',
    methods=['GET', 'POST'])
@app.route(
    '/restaurant/<int:restaurant_id>/menu/',
    methods=['GET', 'POST'])
def showMenu(restaurant_id):
    """This method should retrieve all the menu items
    of a restaurants from the database and show them to the users"""

    restaurant = session.query(Restaurant).filter_by(
        id=restaurant_id).one()

    items = session.query(MenuItem).filter_by(
        restaurant_id=restaurant_id).all()

    return render_template('menu.html', items=items, restaurant=restaurant)


# Create new menu item route
@app.route(
    '/restaurant/<int:restaurant_id>/menu/new',
    methods=['GET', 'POST'])
def newMenuItem(restaurant_id):
    """This method should Create a new menu item for a restaurant
    and save it to the database"""

    restaurant = session.query(Restaurant).filter_by(
        id=restaurant_id).one()

    if request.method == 'POST':
        newItem = MenuItem(
            name=request.form['name'],
            price=request.form['price'],
            description=request.form['description'],
            course=request.form['course'],
            restaurant_id=restaurant_id)

        session.add(newItem)
        session.commit()
        flash('Menu Item " %s " is Successfully Added!' % newItem.name)
        return redirect(url_for('showMenu', restaurant_id=restaurant_id))
    else:
        return render_template(
            'newMenuItem.html', restaurant=restaurant)


# Edit a menu item route
@app.route(
    '/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit',
    methods=['GET', 'POST', 'PUT'])
def editMenuItem(restaurant_id, menu_id):
    """This method should Update or Edit a menu item of a restaurant
    and save the changes to the database"""

    restaurant = session.query(Restaurant).filter_by(
        id=restaurant_id).one()

    editedItem = session.query(MenuItem).filter_by(
        id=menu_id).one()

    if request.method == 'POST':
        editedItem.name = request.form['name']
        editedItem.price = request.form['price']
        editedItem.description = request.form['description']
        editedItem.course = request.form['course']

        session.add(editedItem)
        session.commit()
        flash('Menu Item " %s " is Successfully Edited!' % editedItem.name)
        return redirect(url_for('showMenu', restaurant_id=restaurant_id))
    else:
        return render_template(
            'editMenuItem.html', restaurant=restaurant, item=editedItem)


# Delete a menu item route
@app.route(
    '/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete',
    methods=['GET', 'POST', 'Delete'])
def deleteMenuItem(restaurant_id, menu_id):
    """This method should Delete a menu item of a restaurant
    from the database"""

    restaurant = session.query(Restaurant).filter_by(
        id=restaurant_id).one()

    deletedItem = session.query(MenuItem).filter_by(
        id=menu_id).one()

    if request.method == 'POST':
        session.delete(deletedItem)
        session.commit()
        flash('Menu Item " %s " is Successfully Deleted!' % deletedItem.name)
        return redirect(url_for('showMenu', restaurant_id=restaurant_id))
    else:
        return render_template(
            'deleteMenuItem.html', restaurant=restaurant, item=deletedItem)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
