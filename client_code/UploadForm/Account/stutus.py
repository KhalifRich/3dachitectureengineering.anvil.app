from ._anvil_designer import UserProfileTemplate
import anvil.server
import anvil.users

class UserProfile(UserProfileTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        
        # Fetch the current user and update their status in the profile
        self.update_user_status()

    def update_user_status(self):
        """Fetch the current user's status from the server and update the text box color accordingly."""
        user = anvil.users.get_user()
        
        if user:
            status = anvil.server.call('get_user_status', user['username'])  # Call server function to get status
            self.textbox_status.text = status

            # Update the text color based on the status
            if status == "approved":
                self.textbox_status.foreground = "green"
            elif status == "waiting":
                self.textbox_status.foreground = "yellow"
            elif status == "revoked":
                self.textbox_status.foreground = "red"
            elif status == "active":
                self.textbox_status.foreground = "blue"
        return      