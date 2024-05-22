import anvil.server
from ._anvil_designer import UploadFormTemplate
from anvil import open_form
# Define the main form class for the app
class UploadForm(UploadFormTemplate):
    def __init__(self, **properties):
        # Set the properties of the form
        self.init_components(**properties)

        # Design the layout of the form
        self.title_label = Label(text="3D Architecture Engineering Research App", font=("Arial", 20))
        self.file_loader = FileLoader(accept=".fbx, .stl, .iges, .obj, .collada, .step, .3ds")
        self.upload_button = Button(text="Upload File", role="primary", icon="fa:upload")
        self.upload_button.set_event_handler("click", self.upload_button_click)
        self.notification = Notification()

        # Add components to the form
        self.add_component(self.title_label)
        self.add_component(self.file_loader)
        self.add_component(self.upload_button)
        self.add_component(self.notification)

        # Connect to the existing database and tables
        self.users_table = anvil.server.database['users']  # Assuming 'users' is the name of the table

    # Event handler for upload button click
    def upload_button_click(self, **event_args):
        try:
            # Get the uploaded file data
            file_data = self.file_loader.file

            # Process the uploaded file (you can send it to the server for further processing)
            if file_data:
                self.notification.text = "File uploaded successfully!"
                self.notification.show()

                # Remove the current form from the UI
                self.remove_from_parent()

                # Display the next widget (replace WidgetClass with the class of your next widget)
                next_widget = UploadFormTemplate()
                next_widget.show()
            else:
                self.notification.text = "Please select a file to upload."
                self.notification.show()
        except Exception as e:
            # Handle any errors that may occur during file upload or processing
            self.notification.text = f"An error occurred: {str(e)}"
            self.notification.show()

# Define the Upload class

    def subscribe_show(self, **event_args):
      """This method is called when the Button is shown on the screen"""
      pass

    def file_loader_1_show(self, **event_args):
      """This method is called when the FileLoader is shown on the screen"""
      pass

    def file_loader_1_change(self, file, **event_args):
      """This method is called when a new file is loaded into this FileLoader"""
      pass
class Upload(UploadFormTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        # Any code you write here will run before the form opens.
          # In UploadForm
class UploadFormForm(UploadFormTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
        self.repeating_panel_1.item_template = UploadFormTemplateForm

        # Initialize an empty list to store 3D object info
        self.objects_list = []

    def file_loader_1_change(self, file, **event_args):
        # Handle file upload, assuming file contains 3D object info
        # Here you might want to process the file and extract necessary info
        # For demonstration, we will just use a placeholder image and name
        new_object = {
            'image': 'https://via.placeholder.com/150',  # Placeholder image
            'name': file.name
        }
        self.objects_list.append(new_object)
        self.repeating_panel_1.items = self.objects_list

    def register_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('Register')
        pass
    
    def sign_in_click(self, **event_args):
        """This method is called when the button is clicked"""
        # Implement sign-in functionality
        pass
      # In TileForm
class UploadForm(UploadFormTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)

    def form_show(self, **event_args):
        # This method is called when the form is shown on the screen
        self.image_1.source = self.item['image']
        self.label_1.text = self.item['name']
    
    def download_click(self, **event_args):
        # Booking logic here
      def create_checkout_session():
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                user_registration=[{
                    'price': 'your_price_id',
                }],
                mode='payment',
                success_url='https://3darchitectureengineering.anvil.app/success',
                cancel_url='https://3darchitectureengineering.anvil.app/cancel',
            )

    def button_subscribe_click(self, **event_args):
        session_id = anvil.server.call('create_checkout_session')
        # Redirect the user to the Stripe Checkout session
        self.link_checkout.url = f'https://checkout.stripe.com/en/pay/{session_id}'

        alert(f"Booking {self.item['name']}")

    def subscribe_click(self, **event_args):
        """This method is called when the button is clicked"""
        @anvil.server.callable
        def create_checkout_session():
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                user_registration=[{
                    'price': 'your_price_id',
                }],
                mode='payment',
                success_url='https://3darchitectureengineering.anvil.app/success',
                cancel_url='https://3darchitectureengineering.anvil.app/cancel',
            )

    def button_subscribe_click(self, **event_args):
        session_id = anvil.server.call('create_checkout_session')
        # Redirect the user to the Stripe Checkout session
        self.link_checkout.url = f'https://checkout.stripe.com/en/pay/{session_id}'
