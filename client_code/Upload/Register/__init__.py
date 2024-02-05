from ._anvil_designer import RegisterTemplate
from anvil import *
import anvil.server
import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Register(Upload.RegisterTemplate):
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

        self.clear_inputs()
# In the Form Code section

class Sign_up(Upload.RegisterTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)

    def register_button_click(self, **event_args):
        # Get user input
        username = self.username_textbox.text
        email = self.email_textbox.text
        password = self.password_textbox.text

        # Call the server-side function
        try:
            new_user = anvil.server.call('register_user', username, email, password)
            print(f"User {new_user['username']} registered successfully!")
        except Exception as e:
            print(f"Registration failed: {str(e)}")
