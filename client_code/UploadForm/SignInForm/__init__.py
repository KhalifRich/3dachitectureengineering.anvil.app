# Import necessary modules
from ._anvil_designer import SignInFormTemplate
import anvil.server
import anvil.users
from anvil import open_form, alert, js

# Class definition for SignInForm
class SignInForm(SignInFormTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        anvil.users.get_user()

    # Method to handle sign-in button click
    def sign_in_click(self, email, password):
        # Validate email and password (e.g., check for empty fields)
        if not email or not password:
            alert("Please enter both email and password.")
            return

        # Call the server function to authenticate the user
        user_authenticated = self.authenticate_user(email, password)
        if user_authenticated:
            # Successful login
            open_form('UploadForm')  # Open the home form upon successful login
        else:
            alert("Incorrect email or password.")

    # Server function to authenticate the user
    def authenticate_user(self, email, password):
        user = anvil.server.call('get_user', email=email)
        if user and user['password'].check_password(password):
            return True  # Authentication successful
        else:
            return False  # Authentication failed

    # Function to handle opening the sign-in form
    def open_sign_in_form(self):
        open_form('SignInForm')  # Corrected the function definition to include 'self'

    # Linking button click event to JavaScript function
    def sign_in_click(self, **event_args):
        js.open_sign_in_form()

    # Method to handle enter key press in username text box
    def email_click(self, **event_args):
        """This method is called when the user presses Enter in the username text box"""
        # Fetch the username entered by the user
        username = self.text_email.text
        
        # Move the focus to the email text box
        self.password.focus()

    # Method to handle enter key press in email text box
    def password_click(self, **event_args):
        """This method is called when the user presses Enter in the email text box"""
        # Fetch the email entered by the user
        email = self.password.text

        # Attempt to sign in the user
        password = self.password.text  # Assuming there is a password text box
        try:
            user_authenticated = self.authenticate_user(email, password)
            if user_authenticated:
                # Successful login
                open_form('UploadForm')  # Open the home form upon successful login
            else:
                alert("User does not exist. Please check your email or sign up.")
        except anvil.users.NoSuchUserError:
            # If the user does not exist, display an error message
            alert("User does not exist. Please check your email or sign up.")

    # Method to handle the button click event
    def sign_in_click(self, **event_args):
        """This method is called when the button is clicked"""
        email = self.email.text
        password = self.password.text  # Assuming there is a password text box
        self.sign_in_click(email, password)

    # Method to handle form show event
    def form_show(self, **event_args):
        """This method is called when the form is shown on the page"""
        self.email.focus()

    # Method to handle enter key press in the email text box
    def email_pressed_enter(self, **event_args):
        """This method is called when the user presses Enter in this text box"""
        self.sign_in_click()

    # Method to handle the email text box being shown on the screen
    def email_show(self, **event_args):
        """This method is called when the TextBox is shown on the screen"""
        self.password.focus()

    # Method to handle the password text box being shown on the screen
    def password_show(self, **event_args):
        """This method is called when the TextBox is shown on the screen"""
        self.email.focus()

    # Method to handle button click event
    def sign_in_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('UploadForm')  # Assuming there is a RegisterForm to handle new registrations

    # Method to handle button being shown on the screen
    def register_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('SignUpForm')  # Assuming there is a RegisterForm to handle new registrations
@anvil.server.http_endpoint('/stripe/webhook', methods=['POST'])
def stripe_webhook(**payload):
    event = stripe.Event.construct_from(payload, stripe.api_key)

    if event['type'] == 'transfer.created':
        transfer = event['data']['object']
        print(f"Transfer created: {transfer['id']}")
    # Handle other event types...

    return "Success"
# Other code remains unchanged
