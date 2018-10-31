#!/usr/bin/env python2.7


from flask import Flask, render_template

app = Flask(__name__)


# Get all restaurants route
@app.route('/', methods=['GET'])
@app.route('/restaurants')
def showRestaurants():
    """This method should retrieve all restaurants
    from the database and show them to the users"""
    return render_template('restaurants.html')


# Create restaurant route
@app.route(
    '/restaurant/new',
    methods=['GET', 'POST'])
def newRestaurant():
    """This method should Create a new restaurant
    and save it to the database"""
    return render_template('newRestaurant.html')


# Edit restaurant route
@app.route(
    '/restaurant/<int:restaurant_id>/edit',
    methods=['GET', 'POST'])
def editRestaurant(restaurant_id):
    """This method should Update or Edit a restaurant
    and save the changes to the database"""
    return render_template('editRestaurant.html')


# Delete restaurant route
@app.route(
    '/restaurant/<int:restaurant_id>/delete',
    methods=['GET', 'POST', 'Delete'])
def deleteRestaurant(restaurant_id):
    """This method should Delete a restaurant from the database"""
    return render_template('deleteRestaurant.html')


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
    return render_template('menu.html')


# Create new menu item route
@app.route(
    '/restaurant/<int:restaurant_id>/menu/new',
    methods=['GET', 'POST'])
def newMenuItem(restaurant_id):
    """This method should Create a new menu item for a restaurant
    and save it to the database"""
    return render_template('newMenu.html')


# Edit a menu item route
@app.route(
    '/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit',
    methods=['GET', 'POST', 'PUT'])
def editMenuItem(restaurant_id, menu_id):
    """This method should Update or Edit a menu item of a restaurant
    and save the changes to the database"""
    return render_template('editMenu.html')


# Delete a menu item route
@app.route(
    '/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete',
    methods=['GET', 'POST', 'Delete'])
def deleteMenuItem(restaurant_id, menu_id):
    """This method should Delete a menu item of a restaurant
    from the database"""
    return render_template('deleteMenu.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
