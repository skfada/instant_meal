# INSTANT MEAL
The Instant Meal is a team work project demo with respect to our learning in ALX Africa.

we are using this project to demonstrate what we have learnt so far with respect to software engineering in solving real world problems for people who are so occupied with activities that they do not have time to prepare meal for themselves.

The application also, will assist restaurant owners with respect of their online presence, thereby reaching more customers in order to generate more revenue as they meet the expectations of their online customers via the Instant Meal application

The Instant Meal will serve as a market place for restaurant Owners and for various users to sell and buy their prepared meals at a competative delivery time frame respectfully.


## STEPS TO USE THE APPLICATION

##### 1- CLONE THE REPOSITORY
- clone the repositotory via https://github.com/skfada/instant_meal.git
- navigate into the instant_meal/ directory.

##### 2- SQLITE3 DATABASE
- type the command `./create_all_table.py` to create the sqlite3 database and tables.


##### 3- EXECUTE THE RUN.PY SCRIPT
- type the command `python3 run.py` or `./run.py` in your console to launch the application
- copy the url from the console eg `http://127.0.0.1:5000` and paste to your browser for usage.


## FILE ORGANIZATION

##### instant_meal/
in this repositoty, you will find two items that includes:
- **instant_meal/main/**:
  the main folder contains the flask application and other folders.

- **instant_meal/run.py**:
  this is the script file that will be used to lauch the application for usage by simply running the command `./run.py` in a Linux shell while inside the **instant_meal/** directory



##### instant_meal/main
in the `instant_meal/main` directory, the following folders will be found:


- **instant_meal/main/database/**:


- **instant_meal/main/market_routes/**:


- **instant_meal/main/routes/**:


- **instant_meal/main/static**:
	the `instant_meal/main/static` contains files such as the javascript, css and image files for the whole application.

- **instant_meal/main/templates**:
	the `instant_meal/main/templates` contains the html files for all the response from the routes.
	the templates directory has also been categorized into the:
	- `instant_meal/main/templates/user/`: which will serve all users html response.
	- `instant_meal/main/templates/seller/`: which will serve all sellers html response.
	- `instant_meal/main/templates/market/`: which will serve all market html response.

	- `instant_meal/main/templates/base.html`: this is an html file that will serve as a base template for all the html files in the template directory.

	- `instant_meal/main/templates/home.html`: this is the home html file that will serve as a base template for all the html files that will be diliveres as our index page or home page.




- **instant_meal/main/users_routes/**:



## ROUTING

##### LIST OF API ENDPOINTS OR FUNCTION/METHODS THAT WE WILL BE CREATING TO ALLOW  OTHER CLIENTS TO USE

**1. User Routes**:
   - `/user/register` (POST): Register a new user.
   - `/user/login` (POST): Authenticate and generate a token for the user.
   - `/user/password_reset` (PUT, POST): Reset user password.
   - `/user/update` (PUT, POST): Update user profile information.
   - `/user/dashboard` (GET): to help the user access other user links.
   - `/user/info` (GET): Get the profile information for the authenticated user.
   - `/user/fund_wallet` (POST): to enable users fund their account for transaction purspose.


##### ROUTES YET TO BE IMPLEMENTED OR UPDATED
**3. Market
	- `/api/market`

2. Restaurant Information:
   - `/api/restaurants` (GET): Get a list of all available restaurants.
   - `/api/restaurants/{id}` (GET): Get details about a specific restaurant.

3. Menu Operations:
   - `/api/menu/{restaurant_id}` (GET): Get the menu for a specific restaurant.
   - `/api/menu/{restaurant_id}/items` (POST): Add a new item to the menu.
   - `/api/menu/{restaurant_id}/items/{item_id}` (PUT): Update details of a menu item.
   - `/api/menu/{restaurant_id}/items/{item_id}` (DELETE): Remove a menu item.

4. Order Management:
   - `/api/orders` (GET): Get a list of orders for the authenticated user.
   - `/api/orders/{order_id}` (GET): Get details about a specific order.
   - `/api/orders` (POST): Place a new order.
   - `/api/orders/{order_id}/cancel` (PUT): Cancel a specific order.


6. Cart Operations:
   - `/api/cart` (GET): Get the current contents of the user's shopping cart.
   - `/api/cart/add` (POST): Add items to the user's shopping cart.
   - `/api/cart/remove` (PUT): Remove items from the user's shopping cart.

7. Payment:
   - `/api/payment` (POST): Make a payment for an order.

8. Address Management:
   - `/api/addresses` (GET): Get a list of saved delivery addresses.
   - `/api/addresses` (POST): Add a new delivery address.
   - `/api/addresses/{address_id}` (PUT): Update details of a delivery address.
   - `/api/addresses/{address_id}` (DELETE): Remove a delivery address.

9. Notifications:
   - `/api/notifications` (GET): Get notifications for the user.

10. Search and Filters:
   - `/api/search` (GET): Search for restaurants or menu items.
   - `/api/filters` (GET): Get filtering options for restaurants or menu items.


## AUTHORS
the authors to this project includes:
- OKOLI CHISOM <chisomd90@gmail.com> (https://github.com/chisomd90)
