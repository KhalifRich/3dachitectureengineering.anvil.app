# Import necessary Anvil modules
from anvil import *
import anvil.server

# Define the Register form class
class Register(Upload.RegisterTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.

    def submit_register_click(self, **event_args):
        first_name = self.first_name_box.text
        second_name = self.second_name_box.text
        email = self.email_box.text
        phone = self.phone_box.text
        address = self.address_box.text
        password = self.password_box.text
        confirm_password = self.confirm_password_box.text
        
        # Call the server-side function to register the user
        new_user = anvil.server.call('register_user', first_name, second_name, email, phone, address, password, confirm_password)
        
        Notification("You have successfully registered, You can now enjoy constructing and improve your post-modern architectural skills.", title="Thanks!").show()

        self.clear_inputs()

# Define the Sign_In class
class Sign_In(Sign_InTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.

    def register_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('Register')
        pass
    
    def sign_in_click(self, **event_args):
        """This method is called when the button is clicked"""
        # Implement sign-in functionality
        pass

# Define the Upload class
class Upload(UploadTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        # Any code you write here will run before the form opens.

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

# Define the main form class for the app
class MainAppForm(Form):
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
                next_widget = WidgetClass()
                next_widget.show()
            else:
                self.notification.text = "Please select a file to upload."
                self.notification.show()
        except Exception as e:
            # Handle any errors that may occur during file upload or processing
            self.notification.text = f"An error occurred: {str(e)}"
            self.notification.show()
