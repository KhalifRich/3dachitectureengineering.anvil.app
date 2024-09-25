import anvil.email
import anvil.secrets
import anvil.stripe
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


@anvil.server.callable
def create_user(first_name, second_name, phone, address, email, password):
    existing_user = app_tables.users.get(email=email)
    if existing_user:
        raise anvil.users.UserExists("A user with this email already exists.")
    app_tables.users.add_row(first_name=first_name, second_name=second_name, phone=phone,
                             address=address, email=email, password=anvil.users.generate_password_hash(password))

@anvil.server.callable
def authenticate_user(email, password):
    user = app_tables.users.get(email=email)
    if user and anvil.users.check_password(password, user['password']):
        return user
    else:
        return None

@anvil.server.callable
def initiate_download(product_id):
    product_details = app_tables.products.get(id=product_id)
    session = anvil.stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': product_details['name'],
                },
                'unit_amount': product_details['price'] * 100,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=anvil.server.get_api_origin() + '/checkout/success',
        cancel_url=anvil.server.get_api_origin() + '/checkout/cancel',
    )
    return session.id

@anvil.server.http_endpoint('/checkout/success')
def checkout_success():
    return {'status': 'success'}

@anvil.server.http_endpoint('/checkout/cancel')
def checkout_cancel():
    return {'status': 'cancelled'}
