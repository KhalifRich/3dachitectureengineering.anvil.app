import anvil.stripe
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import stripe

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
stripe.api_key = 'pk_test_51OVEBOJSA1HIvKzySaMh8c9BmuUOahNmC0zRj2m6QxqQ1wLBFvzUo74KYRxbqiutVg7rVMCAiYXBsFTaaHb7nwVo00305E7PZH'

@anvil.server.callable
def process_payment(token, amount):
    try:
        payment_intent = stripe.PaymentIntent.create(
            amount=int(amount * 100),  # Convert amount to cents
            currency='usd',
            payment_method=token,
            confirmation_method='manual',
            confirm=True,
        )
        return payment_intent.client_secret
      
    except stripe.error.CardError as e:
        # Handle card errors
        return str(e)
