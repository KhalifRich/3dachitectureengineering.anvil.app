import anvil.email
import anvil.secrets
import anvil.stripe
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
@anvil.server.callable
def update_user_status(username, status):
    # Fetch user details from the database
    user = app_tables.users.get(username=username)
    
    if user:
        # Update user status
        user['status'] = status
        return True
    else:
        return False
