import anvil.server
from anvil.tables import app_tables

# Server function for user registration
@anvil.server.callable
def register_user(first_name, last_name, phone, address, password):
    try:
        # Check if username or email is already taken
        if app_tables.users.get(first_name=first_name) or app_tables.users.get(email=email):
            raise ValueError("Username or email is already taken.")

        # Hash the password (you should use a secure hashing library in a real application)
        hashed_password = password  # Replace with actual hashing code

        # Store user information in the database
        new_user = app_tables.users.add_row(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            address=address,
            password=hashed_password
        )
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
            new_user = register_user(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                address=address,
                password=password  # You should hash passwords for security
            )
            # Open the home form upon successful registration
            # Transition to the next form (if needed)
            open_form('NextForm')
            open_form('UploadForm')
        except ValueError as ve:
            alert(f"Error registering user: {str(ve)}")