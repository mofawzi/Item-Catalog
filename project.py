#!/usr/bin/env python2.7


from flask import Flask

app = Flask(__name__)


# Get all restaurants route
@app.route('/', methods=['GET'])
@app.route('/restaurants')
def showRestaurants():
    """This method should retrieve all restaurants
    from the database and show them to the users"""
    return 'This is the main page'


# Create restaurant route
@app.route(
    '/restaurant/new',
    methods=['GET', 'POST'])
def newRestaurant():
    """This method should Create a new restaurant
    and save it to the database"""
    return 'New restaurant is created!'


# Edit restaurant route
@app.route(
    '/restaurant/<int:restaurant_id>/edit',
    methods=['GET', 'POST'])
def editRestaurant(restaurant_id):
    """This method should Update or Edit a restaurant
    and save the changes to the database"""
    return 'The restaurant is updated!'


# Delete restaurant route
@app.route(
    '/restaurant/<int:restaurant_id>/delete',
    methods=['GET', 'POST', 'Delete'])
def deleteRestaurant(restaurant_id):
    """This method should Delete a restaurant from the database"""
    return 'The restaurant is deleted!'


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
    return 'This is a menu of a restaurant'


# Create new menu item route
@app.route(
    '/restaurant/<int:restaurant_id>/menu/new',
    methods=['GET', 'POST'])
def newMenuItem(restaurant_id):
    """This method should Create a new menu item for a restaurant
    and save it to the database"""
    return 'New menu item is created!'


# Edit a menu item route
@app.route(
    '/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit',
    methods=['GET', 'POST', 'PUT'])
def editMenuItem(restaurant_id, menu_id):
    """This method should Update or Edit a menu item of a restaurant
    and save the changes to the database"""
    return 'The menu item is updated!'


# Delete a menu item route
@app.route(
    '/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete',
    methods=['GET', 'POST', 'Delete'])
def deleteMenuItem(restaurant_id, menu_id):
    """This method should Delete a menu item of a restaurant
    from the database"""
    return 'The menu item is deleted!'


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
