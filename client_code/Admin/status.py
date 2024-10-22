from ._anvil_designer import AdminPanelTemplate
import anvil.server
from anvil import alert

class AdminPanel(AdminPanelTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
    
    def update_status_click(self, **event_args):
        """Called when the 'Update Status' button is clicked"""
        username = self.text_box_username.text
        if not username:
            alert("Please enter a username.")
            return
        
        # Capture the status selected from checkboxes
        status = None
        if self.checkbox_activate.checked:
            status = "activate"
        elif self.checkbox_revoke.checked:
            status = "revoke"
        elif self.checkbox_approve.checked:
            status = "approve"
        elif self.checkbox_waiting.checked:
            status = "waiting"
        
        if not status:
            alert("Please select a status.")
            return

        # Call server function to update user status
        result = anvil.server.call('update_user_status', username, status)
        if result:
            alert(f"Status of {username} updated to {status}.")
        else:
            alert(f"Failed to update status for {username}. Please check if the user exists.")
