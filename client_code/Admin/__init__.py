from anvil import *
import anvil.server

class AdminPanel(AdminPanelTemplate):

    def __init__(self, **properties):
        self.init_components(**properties)
        self.refresh_user_data()

    def refresh_user_data(self):
        self.repeating_panel_1.items = anvil.server.call('get_all_users')

    def status_dropdown_change(self, **event_args):
        # Called when the user makes a selection
        pass

    def update_button_click(self, **event_args):
        selected_items = self.repeating_panel_1.get_components()
        for item in selected_items:
            user_id = item.item['id']
            new_status = item.status_dropdown.selected_value
            if new_status:
                result = anvil.server.call('update_user_status', user_id, new_status)
                alert(result)
        self.refresh_user_data()
        # Bind this template to the item
        self.item_bindings = {
            'email_label': 'email',
            'status_dropdown': 'status'
        }

    def status_dropdown_change(self, **event_args):
        # Handle status change
        pass
