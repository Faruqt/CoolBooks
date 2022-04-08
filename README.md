# Cool Books

## Features
   - User Profile - Basic info + book preferences
   - New books - a catalogue of books to buy
   - Marketplace - A place where users can swap their books

## Project Structure
The Applicaition comprises of 3 microservices: 
* [user-service](https://cookbooks-user.herokuapp.com/)
* [catalogue-service](https://coolbooks-catalogue.herokuapp.com/)
* [market-place-service](https://coolbooks-market.herokuapp.com/)


## Application Setup and Configuration
To launch the end-to-end microservices application perform the following:


### Step 1.
Create a new Docker network and name it ```cbooks_net```:
```
docker network create cbooks_net
```

### Step 2.
Start your containers:
Navigate into each of the services folder and run:
```
docker-compose up
```

### Step 3.
Using any API testing application of your choice. Navigate to the following api end points to explore the microservices. 

- User-service api endpoints:
I.	Create user:  https://cookbooks-user.herokuapp.com/api/user/create (POST)
II.	Login user: https://cookbooks-user.herokuapp.com/api/user/login (POST)
III.	Logout user: https://cookbooks-user.herokuapp.com/api/user/logout (POST)
IV.	Get authenticated user: https://cookbooks-user.herokuapp.com/api/user (GET)
V.	Get single user: https://cookbooks-user.herokuapp.com/api/user/<username>(GET)
VI.	 Get all users: https://cookbooks-user.herokuapp.com/api/users (GET)

- Catalogue-service api endpoints:

I.	Get all books: https://coolbooks-catalogue.herokuapp.com/api/catalogue (GET)
II.	Get single book: https://coolbooks-catalogue.herokuapp.com/api/catalogue/<id>
(GET)
III.	Update Catalogue: (POST)
 	 https://coolbooks catalogue.herokuapp.com/api/catalogue/create

- Market place-service api endpoints:

I.	Create exchange request: (POST)
https://coolbooks-market.herokuapp.com/api/market/exchange
II.	Get proposals:   https://coolbooks-market.herokuapp.com/api/market/proposals (GET)


