from ._anvil_designer import Sign_UpTemplate
from anvil import *
import anvil.server
import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import app_tables


class register(Sign_UpTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.
    
    def first_name_pressed_enter(self, **event_args):
        """This method is called when the user presses Enter in this text box"""
        pass
    
    def second_name_pressed_enter(self, **event_args):
        """This method is called when the user presses Enter in this text box"""
        pass
    
    def phone_pressed_enter(self, **event_args):
        """This method is called when the user presses Enter in this text box"""
        pass
    
    def address_pressed_enter(self, **event_args):
        """This method is called when the user presses Enter in this text box"""
        pass
    
    def email_pressed_enter(self, **event_args):
        """This method is called when the user presses Enter in this text box"""
        pass
    
    def password_pressed_enter(self, **event_args):
        """This method is called when the user presses Enter in this text box"""
        pass
    
    def confirm_password_pressed_enter(self, **event_args):
        """This method is called when the user presses Enter in this text box"""
        pass
    
    def register_click(self, **event_args):
        """This method is called when the button is clicked"""
        pass
      # In the Server Code section

@anvil.server.callable
def new_user(username, email, password, confirmpassword):
    # Validate input
    if not username or not email or not password:
        raise ValueError("Please fill in all fields.")

    # Check if username or email is already taken
    if app_tables.users.get(username=username) or app_tables.users.get(email=email):
        raise ValueError("Username or email is already taken.")

    # Hash the password (you should use a secure hashing library in a real application)
    hashed_password = password  # Replace with actual hashing code

    # Store user information in the database
    new_user = app_tables.users.add_row(username=username, email=email, password=hashed_password)

    return new_user

    
    def submit_register_click(self, **event_args):
        first_name = self.first_name_box.text
        second_name = self.second_name_box.text
        email = self.email_box.text
        phone = self.phone_box.text
        address = self.address_box.text
        password = self.password_box.text
        confirm_password = self.confirm_password_box.text
        
        anvil.server.call('new_user', first_name, second_name, email, phone, address, password, confirm_password)
        
        Notification("You have successfully registered, You can now enjoy constructing and improve your post-modern architectural skills.", title="Thanks!").show()
# Server function for user registration
@anvil.server.callable
def register_user(first_name, second name, phone, email, password):
    try:
        # Check if username or email is already taken
        if app_tables.users.get(first_name, second name=first_name, second name) or app_tables.users.get(email=email):
            raise ValueError("Username or email is already taken.")

        # Hash the password (you should use a secure hashing library in a real application)
        hashed_password = password  # Replace with actual hashing code

        # Store user information in the database
        new_user = app_tables.users.add_row(first_name, second name, email=email, password=hashed_password)
        anvil.server.wait_forever()
        return new_user
    except Exception as e:
        # Handle registration errors
      def register_click(self, **event_args):
    """This method is called when the button is clicked"""
class RegisterForm(RegisterFormTemplate):
    def __init__(self, **properties):
        # Set up this form
        self.init_components(**properties)

    def button_register_click(self, **event_args):
        # Retrieve user input
        first_name = self.text_box_first_name.text
        last_name = self.text_box_last_name.text
        phone = self.text_box_phone.text
        address = self.text_box_address.text
        password = self.text_box_password.text
        confirm_password = self.text_box_confirm_password.text

        # Validate input
        if not all([first_name, last_name, phone, address, password, confirm_password]):
            alert("Please fill in all fields.")
            return

        if password != confirm_password:
            alert("Passwords do not match.")
            return

        # Create user (you would replace this with your actual user creation logic)
        try:
            new_user = app_tables.users.add_row(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                address=address,
                password=hash_password(password)  # You should hash passwords for security
            )
            # Open the home form upon successful registration
           # Transition to the next form (if needed)
            open_form('NextForm')
            open_form('UploadForm')
        except:
            alert("Error registering user. Please try again.")
        pass
        raise ValueError(f"Registration failed: {str(e)}")
        self.clear_inputs()
