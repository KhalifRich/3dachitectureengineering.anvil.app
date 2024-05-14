# Import necessary modules
import anvil.server
from ._anvil_designer import SignInFormTemplate
from anvil import open_form, alert
from anvil.tables import app_tables
from anvil import open_form, js

# Class definition for SignInForm
class SignInForm(SignInFormTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

    # Method to handle sign-in button click
    def sign_in_click(self, email, password):
        # Validate email and password (e.g., check for empty fields)
        if not email or not password:
            alert("Please enter both email and password.")
            return

        # Implement authentication logic (e.g., using Anvil Users service)
        user = app_tables.users.get(email=email)
        if user and user['password'].check_password(password):
            # Successful login
            open_form('UploadForm')  # Open the home form upon successful login
        else:
            alert("Incorrect email or password.")

    # Function to handle opening the sign-in form
    def open_sign_in_form():
        open_form('SignInForm')

    # Linking button click event to JavaScript function
    def button_sign_in_click(self, **event_args):
        js.open_sign_in_form()

    # Other code remains unchanged
