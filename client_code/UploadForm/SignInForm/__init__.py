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
    def open_sign_in_form(self):
        open_form('SignInForm')  # Corrected the function definition to include 'self'

    # Linking button click event to JavaScript function
    def button_sign_in_click(self, **event_args):
        js.open_sign_in_form()

    # Method to handle enter key press in username text box
    def text_box_1_click(self, **event_args):
        """This method is called when the user presses Enter in the username text box"""
        # Fetch the username entered by the user
        username = self.text_box_1.text
        
        # Move the focus to the email text box
        self.text_box_2.focus()

    # Method to handle enter key press in email text box
    def text_box_2_click(self, **event_args):
        """This method is called when the user presses Enter in the email text box"""
        # Fetch the email entered by the user
        email = self.text_box_2.text

        # Attempt to sign in the user
        try:
            user = app_tables.users.get(email=email)
            
            # If the user exists, do something (e.g., navigate to another form)
            open_form('UploadForm')  # Replace 'HomeForm' with the name of your home form
        except anvil.users.NoSuchUserError:
            # If the user does not exist, display an error message
            alert("User does not exist. Please check your email or sign up.")

    # Other code remains unchanged

    def button_2_click(self, **event_args):
      """This method is called when the button is clicked"""
      open_form('Sign_UpForm')
      pass

    def form_show(self, **event_args):
      """This method is called when the form is shown on the page"""
      pass

    def text_box_2_pressed_enter(self, **event_args):
      """This method is called when the user presses Enter in this text box"""
      pass

    def email_show(self, **event_args):
      """This method is called when the TextBox is shown on the screen"""
      pass

    def password_show(self, **event_args):
      """This method is called when the TextBox is shown on the screen"""
      pass

    def button_1_click(self, **event_args):
      """This method is called when the button is clicked"""
      pass

    def button_2_show(self, **event_args):
      """This method is called when the Button is shown on the screen"""
      pass
