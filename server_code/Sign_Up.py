# Import necessary modules
from ._anvil_designer import Sign_UpTemplate
from anvil import open_form, hash_password, alert
import anvil.server
import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class register(Sign_UpTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

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

@anvil.server.callable
def new_user(first_name, second_name, email, phone, address, password, confirm_password):
    try:
        # Validate input
        if not all([first_name, second_name, email, phone, address, password, confirm_password]):
            raise ValueError("Please fill in all fields.")

        # Check if username or email is already taken
        if app_tables.users.get(email=email):
            raise ValueError("Email is already taken.")

        # Hash the password (you should use a secure hashing library in a real application)
        hashed_password = hash_password(password)

        # Store user information in the database
        new_user = app_tables.users.add_row(first_name=first_name, second_name=second_name, email=email, phone=phone, address=address, password=hashed_password)

        return new_user
    except Exception as e:
        # Handle registration errors
        raise ValueError(f"Registration failed: {str(e)}")

@anvil.server.callable
def register_user(first_name, second_name, phone, email, password):
    try:
        # Validate input
        if not all([first_name, second_name, phone, email, password]):
            raise ValueError("Please fill in all fields.")

        # Check if username or email is already taken
        if app_tables.users.get(first_name=first_name, second_name=second_name) or app_tables.users.get(email=email):
            raise ValueError("Username or email is already taken.")

        # Hash the password (you should use a secure hashing library in a real application)
        hashed_password = hash_password(password)

        # Store user information in the database
        new_user = app_tables.users.add_row(first_name=first_name, second_name=second_name, email=email, phone=phone, password=hashed_password)

        return new_user
    except Exception as e:
        # Handle registration errors
        raise ValueError(f"Registration failed: {str(e)}")

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
                second_name=last_name,
                phone=phone,
                address=address,
                password=hash_password(password)  # You should hash passwords for security
            )
            # Open the home form upon successful registration
           # Transition to the next form (if needed)
            open_form('NextForm')
            open_form('UploadForm')
        except Exception as e:
            alert(f"Error registering user. Please try again. {str(e)}")
            return
