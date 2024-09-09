from ._anvil_designer import SignUpFormTemplate
from anvil import open_form, alert
import anvil.server
from anvil import open_form, Label, FileLoader, Button, Notification


class SignUpForm(SignUpFormTemplate):
    def first_name_pressed_enter(self, **event_args):
        """This method is called when the user presses Enter in this text box"""
        self.second_name.focus()

    def second_name_pressed_enter(self, **event_args):
        """This method is called when the user presses Enter in this text box"""
        self.phone.focus()

    def phone_pressed_enter(self, **event_args):
        """This method is called when the user presses Enter in this text box"""
        self.address.focus()

    def address_pressed_enter(self, **event_args):
        """This method is called when the user presses Enter in this text box"""
        self.email.focus()

    def email_pressed_enter(self, **event_args):
        """This method is called when the user presses Enter in this text box"""
        self.password.focus()

    def password_pressed_enter(self, **event_args):
        """This method is called when the user presses Enter in this text box"""
        self.confirm_password.focus()

    def confirm_password_pressed_enter(self, **event_args):
        """This method is called when the user presses Enter in this text box"""
        self.register_click()

    def register_click(self, **event_args):
        """This method is called when the button is clicked"""
        first_name = self.first_name.text
        second_name = self.second_name.text
        phone = self.phone.text
        address = self.address.text
        email = self.email.text
        password = self.password.text
        confirm_password = self.confirm_password.text

        if not all([first_name, second_name, phone, address, email, password, confirm_password]):
            alert("Please fill out all fields.")
            return

        if password != confirm_password:
            alert("Passwords do not match.")
            return

        try:
            # Assuming there's a server function 'create_user' that handles user registration
            anvil.server.call('create_user', first_name, second_name, phone, address, email, password)
            alert("Registration successful!", style="success")
            open_form('SignInForm')  # Redirect to sign-in form after successful registration
        except Exception as e: 
            alert(f"An error occurred: {str(e)}", style="danger")

# Server-side function example for creating a user
def create_user(first_name, second_name, phone, address, email, password):
    existing_user = app_tables.users.get(email=email)
    if existing_user:
        raise anvil.users.UserExists("A user with this email already exists.")
    app_tables.users.add_row(first_name=first_name, second_name=second_name, phone=phone,
                             address=address, email=email, password=anvil.users.generate_password_hash(password))
