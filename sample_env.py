import os
# put your stripe publishable key within the second pair of inverted commas
os.environ.setdefault('STRIPE_PUBLISHABLE', "")
# put your stripe secret key within the second pair of inverted commas
os.environ.setdefault('STRIPE_SECRET', "")
# put your email address within the second pair of inverted commas
os.environ.setdefault('EMAIL_ADDRESS', "")
# put your email app key  within the second pair of inverted commas
os.environ.setdefault('EMAIL_PASSWORD', "")
# put your app secret key within the second pair of inverted commas
os.environ.setdefault('SECRET_KEY','')
# put your database url here
os.environ.setdefault('DATABASE_URL','')
