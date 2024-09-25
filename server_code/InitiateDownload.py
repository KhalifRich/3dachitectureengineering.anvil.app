import anvil.secrets
import anvil.stripe
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from anvil import server, stripe, window

# Define a server function to handle download and checkout
@anvil.server.callable
def initiate_download(product_id):
    # Get product details (price, name, etc.) from the database
    product_details = get_product_details(product_id)
    
    # Initiate checkout session with Stripe
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': product_details['name'],
                },
                'unit_amount': product_details['price'] * 132,  # Stripe requires price in cents
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=anvil.server.get_api_origin() + '/checkout/success',
        cancel_url=anvil.server.get_api_origin() + '/checkout/cancel',
    )
    
    # Return the checkout session ID to the client
    return session.id

# Handle checkout success
@anvil.server.http_endpoint('/checkout/success')
def checkout_success():
    # Handle checkout success
    # Perform actions like marking the product as purchased in the database, sending confirmation emails, etc.
    # You can also initiate the download process here
    return {'status': 'success'}

# Handle checkout cancellation
@anvil.server.http_endpoint('/checkout/cancel')
def checkout_cancel():
    # Handle checkout cancellation
    # Redirect the user back to the product page or show a message
    return {'status': 'cancelled'}