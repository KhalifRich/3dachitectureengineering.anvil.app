import anvil.secrets
import anvil.server
import anvil.media

@anvil.server.callable
def upload_file(file):
    if file.content_type == 'application/pdf':
        app_table = anvil.tables.app_tables.applications
        app_table.add_row(file=file)
        return "File uploaded successfully"
    else:
        return "Only PDF files are accepted"
