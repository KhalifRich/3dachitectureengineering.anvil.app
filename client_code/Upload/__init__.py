from ._anvil_designer import UploadTemplate
from anvil import *

class Upload(UploadTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    {
    'Upload':forms.FileInputs(attrs = {'accept':'.fbx, .stl, .iges, .obj, .collada, .step, .3ds'})
    }
    pass