import anvil.server
from ._anvil_designer import UploadFormTemplate
from anvil import open_form
from anvil import Label, FileLoader, Button, Notification

# Define the main form class for the app
class UploadForm(UploadFormTemplate):
    def __init__(self, **properties):
        # Set the properties of the form
        self.init_components(**properties)

        # Design the layout of the form
        self.title_label = Label(text="3D Architecture Engineering Research App", font=("Arial", 20))
        self.file_loader = FileLoader(accept=".fbx, .stl, .iges, .obj, .collada, .step, .3ds")
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

    # Event handler for upload button click
    def upload_button_click(self, **event_args):
        try:
            # Get the uploaded file data
            file_data = self.file_loader.file

            # Process the uploaded file (you can send it to the server for further processing)
            if file_data:
                self.notification.text = "File uploaded successfully!"
                self.notification.show()

                # Transition to the next form
                open_form('NextForm')  # Replace 'NextForm' with the actual name of your next form
            else:
                self.notification.text = "Please select a file to upload."
                self.notification.show()
        except Exception as e:
            # Handle any errors that may occur during file upload or processing
            self.notification.text = f"An error occurred: {str(e)}"
            self.notification.show()

    # Event handlers for other components (if needed)
    def subscribe_show(self, **event_args):
        pass  # Implement functionality if needed

    def file_loader_1_show(self, **event_args):
        pass  # Implement functionality if needed

    def file_loader_1_change(self, file, **event_args):
        pass  # Implement functionality if needed

    def subscribe_click(self, **event_args):
        """This method is called when the button is clicked"""
        pass

class Upload(UploadFormTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Initialize an empty list to store 3D object info
        self.objects_list = []

    def file_loader_1_change(self, file, **event_args):
        # Handle file upload, assuming file contains 3D object info
        # For demonstration, we will just use a placeholder image and name
        new_object = {
            'image': 'https://via.placeholder.com/150',  # Placeholder image
            'name': file.name
        }
        self.objects_list.append(new_object)
        self.repeating_panel_1.items = self.objects_list

    def register_click(self, **event_args):
        open_form('Register')

    def sign_in_click(self, **event_args):
        pass  # Implement sign-in functionality

class TileForm(UploadFormTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)

    def form_show(self, **event_args):
        self.image_1.source = self.item['image']
        self.label_1.text = self.item['name']
    
    def download_click(self, **event_args):
        pass  # Booking logic here

    def create_checkout_session(self):
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            user_registration=[{
                'price': 'your_price_id',
            }],
            mode='payment',
            success_url='https://3darchitectureengineering.anvil.app/success',
            cancel_url='https://3darchitectureengineering.anvil.app/cancel',
        )
        return session.id

    def button_subscribe_click(self, **event_args):
        session_id = anvil.server.call('create_checkout_session')
        self.link_checkout.url = f'https://checkout.stripe.com/en/pay/{session_id}'
        alert(f"Booking {self.item['name']}")
