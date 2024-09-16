from ._anvil_designer import UploadFormTemplate
from anvil import open_form, alert, Button, FileLoader, Label, Notification
import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.stripe
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from ._anvil_designer import SignInFormTemplate
from anvil import open_form, alert, js

anvil.server.connect("client_PZ7EIGSDEHWYW4J7KFNUCKCK-O4K32GQTI5IPOBJ7")
# Function to authenticate user
@anvil.server.callable
def authenticate_user(username_or_email, password):
    # Here you would perform the authentication logic, such as checking the username/email and password against your database
    # For demonstration purposes, let's assume a simple check
    if username_or_email == 'test_user' and password == 'password123':
        return True
    else:
        open_form('SignUpForm')
        raise Exception('Invalid username/email or password')
