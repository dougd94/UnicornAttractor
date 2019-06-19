# Unicorn Attractor
[![Build Status](https://travis-ci.org/dougd94/UnicornAttractor.svg?branch=master)](https://travis-ci.org/dougd94/UnicornAttractor)

## [Deployed Website Link](https://unicorn-attractor-1.herokuapp.com)

##  Test Card
### Important
For testing buying features and features upvotes. 
Use card number 4242424242424242
Any cvc number of three digits 
and any expiry date in the future.

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
* Admins can change the status (from the choices: To Do, Doing and Fininshed) within the admin panel

## Technologies Used

* Cloud 9
* Html 5
* Css
* Jquery
* Charts.js
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
* Checkout 66%

### Manual Testing
Non Logged in user:
* Should only see Home Features Bugs Cart Register Log In in the navbar.
* should be redirected to log in if they click cart
* I clicked all of these to see the correct template was used.
* I tried to register with passwords that didnt match I got an error.
* I tried to register with an already used email and username and I got errors.
* I attempted to register with unique name and email and matching passwords, and was successful.
* I attempted to get in the checkout by entering the url and was redirected to log in.

Logged in user:
* Should see Home Features Bugs Cart Profile Log-Out in the navbar
* I created bugs and features
* I upvoted bugs to see that I could only vote once
* I purchased features and saw that after purchase you could upvote as many times as you want.
* I commented on things.

I opened the website in developer tools and checked how it looked in a variety of devices.

I opened it in firefox and chrome and saw no major issues.

I found that you could register without putting in an email address, I fixed this.

I was happy with the result.

### Bugs
when you remove something from the cart it pops back in, I did not have time to fix this.


## To run locally (on cloud 9)

Set up a virtual env by copying this into your terminal "wget -q https://git.io/v77xs -O /tmp/setup-workspace.sh && source /tmp/setup-workspace.sh" without the inverted commas.

To install your requirements from requirements.txt file

"pip3 install -r requirements.txt"

You will need to create a env.py file. .gitignore your env file as it contains senstive info.

You will need to create an env file, [see sample env file](../sample_env.py)

You will need to create a SECRET_KEY and Stripe keys.

You can comment out

os.environ.setdefault('DATABASE_URL', '') in your env.py file, you will eventually need postgres which you can get on herkou.

You will need to type to migrate your data to database:

python3 ./manage.py makemigrations

python3 ./manage.py migrate
./manage.py createsuperuser (I reccomend the username Admin, as this is your admin account)

you can access the admin panel at /admin once your site is running


Copy to your terminal: "python3 manage.py collectstatic"

This will allow whitenoise to create a staticfiles directory which is neccesary for deployment

To run the server copy this to the terminal: "python3 manage.py runserver $IP:$C9_PORT"

## Deployment
* Create an account and then app on heroku 
* follow the instructions by copying the terminal commands to connect to heroku git
* add the postgres addon
* copy the database url into your env file

### Config Variables
Copy everything from env.py into your config variables. ex: "STRIPE_PUBLISHABLE" : "12424"

add DISABLE_COLLECTSTATIC set it to 1

Follow the migration procedure from the run locally section

On cloud9 do: git add . then do a git commit ( git commit -m "message") a git push

You can now push to heroku with the following command

git push heroku master