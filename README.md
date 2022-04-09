# Cool Books

## Features
   - User Profile - Basic info + book preferences
   - New books - a catalogue of books to buy
   - Marketplace - A place where users can swap their books

## Project Structure
The Application comprises of 3 microservices: 
* [user-service](http://127.0.0.1:5051)
* [catalogue-service](http://127.0.0.1:5053)
* [market-place-service](http://127.0.0.1:5052)

## Application Setup and Configuration
To launch the microservices application perform the following:

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
Using any API testing application of your choice, navigate to the following api end points to test the API endpoints in each micro-service. 

Kindly note: Data from user should be provided as **form-data** 

- User-service api endpoints:

    I. Create user:  http://127.0.0.1:5051/api/user/create (POST)
    
   II.	Login user: http://127.0.0.1:5051/api/user/login (POST)
   
   III.	Logout user: http://127.0.0.1:5051/api/user/logout (POST)
   
   IV. Get authenticated user: http://127.0.0.1:5051/api/user (GET)
   
   V.	Get single user: http://127.0.0.1:5051/api/user/username/(GET)
   
   VI. Get all users: http://127.0.0.1:5051/api/users (GET)

- Catalogue-service api endpoints:

   I.	Get all books: http://127.0.0.1:5053/api/catalogue (GET)
   
   II. Get single book: http://127.0.0.1:5053/api/catalogue/id (GET)

  III. Update Catalogue: http://127.0.0.1:5053/api/catalogue/create (POST)

- Market place-service api endpoints:

   I.	Create exchange request: http://127.0.0.1:5052/api/market/exchange (POST)
   
   II. Get proposals: http://127.0.0.1:5052/api/market/proposals (GET)

## Hosted Project
The 3 microservices have also been hosted on heroku server: 
* [user-service](https://cookbooks-user.herokuapp.com/)
* [catalogue-service](https://coolbooks-catalogue.herokuapp.com/)
* [market-place-service](https://coolbooks-market.herokuapp.com/)
   
