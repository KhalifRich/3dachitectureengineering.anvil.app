import anvil.server
from anvil.tables import app_tables
from anvil import hash_password, open_form, alert

class RegisterForm:
    def __init__(self, **properties):
        self.init_components(**properties)

    def button_register_click(self, **event_args):
        first_name = self.text_box_first_name.text
        last_name = self.text_box_last_name.text
        phone = self.text_box_phone.text
        address = self.text_box_address.text
        email = self.text_box_email.text
        password = self.text_box_password.text
        confirm_password = self.text_box_confirm_password.text

        if not all([first_name, last_name, phone, address, email, password, confirm_password]):
            alert("Please fill in all fields.")
            return

        if password != confirm_password:
            alert("Passwords do not match.")
            return

        try:
            user = app_tables.users.get(email=email)
            if user:
                raise ValueError("Email is already taken.")

            hashed_password = hash_password(password)
            new_user = app_tables.users.add_row(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                address=address,
                email=email,
                password=hashed_password
            )
            open_form('NextForm')
            open_form('UploadForm')
        except Exception as e:
            alert(f"Error registering user. Please try again. {str(e)}")

@anvil.server.callable
def register_user(first_name, last_name, phone, address, email, password):
    try:
        user = app_tables.users.get(email=email)
        if user:
            raise ValueError("Email is already taken.")

        hashed_password = hash_password(password)
        new_user = app_tables.users.add_row(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            address=address,
            email=email,
            password=hashed_password
        )
        return new_user
    except Exception as e:
        raise ValueError(f"Registration failed: {str(e)}")
