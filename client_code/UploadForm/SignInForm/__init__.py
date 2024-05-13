import anvil.server
from ._anvil_designer import SignInFormTemplate
from anvil import open_form, alert
from anvil.tables import app_tables
from anvil import open_form, js
# This code should be placed in your client-side code (e.g., in the Main Form's code behind)
from anvil import open_form, js

class SignInForm(SignInFormTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

    def sign_in_clicked(self, email, password):
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
    def button_register_click(self, **event_args):
        # Open the registration form
        open_form('RegisterForm')
       # Implementing missing event handlers
    def email_pressed_enter(self, **event_args):
        pass

    def password_pressed_enter(self, **event_args):
        pass

    def sign_in_click(self, **event_args):
        pass

    def button_2_click_click(self, **event_args):
        pass

    def button_2_click(self, **event_args):
      """This method is called when the button is clicked"""
      def handle_registration():
    # Open the registration form
    open_form('RegisterForm')
      pass
