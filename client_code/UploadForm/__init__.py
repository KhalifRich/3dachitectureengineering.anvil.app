from ._anvil_designer import UploadFormTemplate
import anvil.server
import anvil.users
from anvil import open_form, Label, FileLoader, Button, Notification


# Define the main form class for the app
class UploadForm(UploadFormTemplate):
    def __init__(self, **properties):
        # Set the properties of the form
        self.init_components(**properties)

        # Design the layout of the form
        self.title_label = Label(text="3D Architecture Engineering Research App", font=("Arial", 20))
        self.file_loader = FileLoader(accept=".fbx,.stl,.iges,.obj,.collada,.step,.3ds")
        self.upload_button = Button(text="Upload File", role="primary", icon="fa:upload")
        self.notification = Notification()

        # Add components to the form
        self.add_component(self.title_label)
        self.add_component(self.file_loader)
        self.add_component(self.upload_button)
        self.add_component(self.notification)
        # Connect to the existing database and tables
        self.users_table = anvil.server.database['users']  # Assuming 'users' is the name of the table

        # Set event handler for upload button click
        self.upload_button.set_event_handler("click", self.upload_button_click)

    def upload_button_click(self, **event_args):
        try:
            file_data = self.file_loader.file
            if file_data:
                self.notification.text = "File uploaded successfully!"
                self.notification.show()
                open_form('NextForm')  # Replace 'NextForm' with the actual name of your next form
            else:
                self.notification.text = "Please select a file to upload."
                self.notification.show()
        except Exception as e:
            self.notification.text = f"An error occurred: {str(e)}"
            self.notification.show()

class Upload(UploadFormTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
        self.objects_list = []

    def upload_change(self, file, **event_args):
        if file:
            new_object = {
                'image': 'https://via.placeholder.com/150',  # Placeholder image
                'name': file.name
            }
            self.objects_list.append(new_object)
            self.repeating_panel_1.items = self.objects_list

    def register_click(self, **event_args):
        open_form('UploadForm.SignUpForm')

    def sign_in_click(self, **event_args):
        try:
            user = anvil.users.login_with_form()
            if user:
                Notification("Sign in successful!", style="success").show()
                open_form('UploadForm')  # Replace 'HomePage' with the actual home page form
            else:
                Notification("Sign in failed. Please try again.", style="danger").show()
        except Exception as e:
            Notification(f"An error occurred: {str(e)}", style="danger").show()

class TileForm(UploadFormTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)

    def form_show(self, **event_args):
        self.image.source = self.item['image']
        self.label_1.text = self.item['name']
    
    def download_click(self, **event_args):
        try:
            file_url = self.item.get('file_url')
            if file_url:
                anvil.server.download(file_url)
                Notification("Download started.", style="info").show()
            else:
                Notification("No file available to download.", style="warning").show()
        except Exception as e:
            Notification(f"An error occurred: {str(e)}", style="danger").show()

    def create_checkout_session(self):
        session = anvil.server.call('create_checkout_session')
        return session.id

    def button_subscribe_click(self, **event_args):
        session_id = self.create_checkout_session()
        self.link_checkout.url = f'https://checkout.stripe.com/en/pay/{session_id}'
        alert(f"Booking {self.item['name']}")
