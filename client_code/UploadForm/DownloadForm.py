import anvil.server
import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
# Inside ProductPage code section
from anvil import js

@self.button_download.click
def button_download_click(self, **event_args):
    # Call the server function to initiate download
    download_session_id = anvil.server.call('initiate_download', self.item['product_id'])
    
    # Redirect user to Stripe checkout page
    js.window.location.href = f"https://checkout.stripe.com/pay/{download_session_id}"