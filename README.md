# Unicorn Attractor
[![Build Status](https://travis-ci.org/dougd94/UnicornAttractor.svg?branch=master)](https://travis-ci.org/dougd94/UnicornAttractor)

## [Deployed Website Link](https://unicorn-attractor-1.herokuapp.com)

___

## UX

* User Story: I want a sign up link on the first page I visit, as im here to make a bug or feature request.
* User Story: I would like to see a breakdown of current feature and bug statistics on the home page.
* User Story: I want to be able to vote on features/bugs that I agree with.
* User Story: I want to create my own features and bugs after I sign up.
* User Story: I can comment on my own and others bugs/features.
* User Story: I am presented with a page full of features and bugs, when I click their respective links. 
* User Story: I can see all the relevant information about the features and bugs, before clicking, but can click into their own pages if I wish.
* User Story: I can see how many views each bug and feature has.
* User Story: The checkout process is simple and effective.
* User Story: All of my features and bugs are available on my profile page.
* User Story: If I forget my password, it's simple to reset it.


[Original Figma Wireframes](https://www.figma.com/file/0OfvfbikzuhJOm73JBHTw5HA/Untitled?node-id=0%3A1)

## Features

* Website intgrated (PostGres)mySQL database.
* Users can create an account
* Users can create and upvote bugs for free.
* Users can create and upvote features, although they must pay.
* Users can comment on any bug or feature.
* Users can use a "forget you password" feature.
* Users can view statistics of current features and bugs on the homepage.

## Technologies Used
* Cloud 9
* Html 5
* Css
* Jquery
* Javascript
* Heroku
* PostGres
* sqlite3
* Bootstrap
* Django
* Python
* Materialize Icons
* Github : Multiple branches and pull requests
* Travis
* Stripe for payments

## Testing 

### Automated

Automated testing and manual testing was used for this project.
Travis Continuous Integration was also utilized.
[The travis page can be visited here](https://travis-ci.org/dougd94/UnicornAttractor) or you can click the badge at the top of the page, 
which shows if the current build is passing.

Django TestCase was used.
I automated test
I installed  coverage (pip3 install coverage)
and ran it for each app (coverage run --source= manage.py test)
then did coverage html to see the percentage for each app.

#### Percent covered
note: I ran this on the entire app. I didn't write tests for stuff like apps.py or admin.py
only Forms.py / Views.py or Models.py
* Accounts 51%
* Bugs 64%
* Features 65%
* Cart 51%
* Checkout 61%

### Manual Testing
Non Logged in user:
* Should only see Home Features Bugs Cart Register Log In in the navbar.
* should be redirected to log in if they click cart
* click all of these to see the correct template was used.
* I tried to register with passwords that didnt match I got an error.
* I tried to register with an already used email and username and I got errors.
* I attempted to register with unique name and email and matching passwords, and was successful.
* I attempted to get in the checkout by entering the url and was redirected to log in.

Logged in user:

