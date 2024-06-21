from ._anvil_designer import AccountTemplate
from anvil import *
import anvil.server
import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Account(AccountTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def upload_button_click(self, **event_args):
        file = self.file_loader.file
        if file:
            if file.content_type == 'application/pdf':
                result = anvil.server.call('upload_file', file)
                alert(result)
            else:
                alert("Please upload a PDF file.")
        else:
            alert("Please select a file to upload.")
@anvil.server.callable
def get_all_users():
    return app_tables.users.search()

@anvil.server.callable
def update_user_status(user_id, new_status):
    user = app_tables.users.get_by_id(user_id)
    if user:
        user['status'] = new_status
        return "Status updated successfully"
    return "User not found"

