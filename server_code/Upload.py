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
from datetime import datetime
from ._anvil_designer import UploadFormTemplate
from anvil import open_form, alert, Link

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42

# Define the UploadForm class
class UploadForm(UploadFormTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
        self.file_loader = FileLoader()
        self.file_loader.set_event_handler("change", self.file_loader_change)

    def file_loader_change(self, file, **event_args):
        # Process the uploaded file
        UPLOAD_CREDIT = 300  # $3 in cents

        @anvil.server.callable
        def upload_project(user_email, project_title):
            user = app_tables.users.get(email=user_email)
            if user:
                project = app_tables.projects.add_row(user=user, title=project_title, credits_earned=UPLOAD_CREDIT)
                user['balance'] = (user['balance'] or 0) + UPLOAD_CREDIT
                return project
        if file:
            alert("File uploaded successfully!")
            # Add your file processing logic here

            # Example: Store file information in Anvil Data Table
            app_tables.uploaded_files.add_row(file_name=file.name, file_data=file.get_bytes())

            # Transition to the next form (if needed)
            open_form('NextForm')
  
# Define the RegisterForm class
class RegisterForm(RegisterFormTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)

    def button_register_click(self, **event_args):
        # Retrieve user input
        first_name = self.text_box_first_name.text
        last_name = self.text_box_last_name.text
        phone = self.text_box_phone.text
        address = self.text_box_address.text
        password = self.text_box_password.text
        confirm_password = self.text_box_confirm_password.text

        # Validate input
        if not all([first_name, last_name, phone, address, password, confirm_password]):
            alert("Please fill in all fields.")
            return

        if password != confirm_password:
            alert("Passwords do not match.")
            return

        # Create user (you would replace this with your actual user creation logic)
        try:
            new_user = anvil.users.signup_with_form(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                address=address,
                password=password
            )
            # Display a link to navigate to the next form upon successful registration
            link_to_next_form = Link(text="Click here to continue", url="#")
            self.add_component(link_to_next_form)

            # Set link click event to open the UploadForm
            link_to_next_form.set_event_handler("click", lambda **event_args: open_form('UploadForm'))
        except anvil.users.AuthenticationFailed:
            alert("Error registering user. Please try again.")
