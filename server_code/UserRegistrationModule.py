import anvil.server
from anvil.tables import app_tables

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