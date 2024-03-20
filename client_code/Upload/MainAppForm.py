# Import necessary Anvil modules
from anvil import *
import anvil.server

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

# Define the next widget class for the app (replace this with your actual next widget class)
class NextWidget(Form):
    def __init__(self, **properties):
        self.init_components(**properties)

        # Design the layout of the next widget
        # Add components and functionality as needed

# Instantiate the main form and display it
main_form = MainAppForm()
main_form.show()