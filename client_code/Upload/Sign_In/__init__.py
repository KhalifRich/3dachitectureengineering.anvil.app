from ._anvil_designer import Sign_InTemplate
from anvil import *
import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class Sign_In(Sign_InTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def email_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def password_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def email_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def sign_in_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
    # Any code you write here will run before the form opens.

  def register_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Register')
    pass
    

  
