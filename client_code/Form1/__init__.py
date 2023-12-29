from ._anvil_designer import Form1Template
from anvil import *
 import os

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
  
fi = form['filename']
if fi.filename:
	# This code will strip the leading absolute path from your file-name
	fil = os.path.basename(fi.filename)
	# open for reading & writing the file into the server
	open(fn, 'wb').write(fi.file.read())
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
