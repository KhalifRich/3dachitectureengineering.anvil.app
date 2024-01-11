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


class Sign_Up(Sign_UpTemplate):
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
    def sign_up_click(self, **event_args):
    """This method is called when the button is clicked"""
    def submit_sign_up_click(self, **event_args):
    first_name = self.first_name_box.text
    second_name = self.second_name_box.text
    email = self.email_box.text
    phone = self.phone_box.text
    address = self.address_box.text
    password = self.password_box.text
    confirm_password = self.confirm_password_box.text
    anvil.server.call('add_user', name, email, phone, address, password, confirm_password)
    Notification("You have successfully registered, You can now enjoy constructing and improve your post modern architectural skills.", title="Thanks!").show()

    self.clear_inputs()
    pass
    


