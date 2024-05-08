from ._anvil_designer import RegisterFormTemplate
from anvil import *
import anvil.server
import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import open_form


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
            open_form('UploadForm')
        except:
            alert("Error registering user. Please try again.")