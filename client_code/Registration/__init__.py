from ._anvil_designer import RegistrationTemplate
from anvil import *
import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Registration(RegistrationTemplate):
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
    

    # Any code you write here will run before the form opens.
def button_2_click(self, **event_args):
    open_form('Registration')
 pass