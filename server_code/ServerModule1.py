import anvil.server
from anvil.tables import app_tables

# Server function for user registration
@anvil.server.callable
def register_user(username, email, password):
    try:
        # Check if username or email is already taken
        if app_tables.users.get(username=username) or app_tables.users.get(email=email):
            raise ValueError("Username or email is already taken.")

        # Hash the password (you should use a secure hashing library in a real application)
        hashed_password = password  # Replace with actual hashing code

        # Store user information in the database
        new_user = app_tables.users.add_row(username=username, email=email, password=hashed_password)
        anvil.server.wait_forever()
        return new_user
    except Exception as e:
        # Handle registration errors
        raise ValueError(f"Registration failed: {str(e)}")