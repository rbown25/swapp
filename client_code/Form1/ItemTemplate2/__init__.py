from ._anvil_designer import ItemTemplate2Template
from anvil import *
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ItemTemplate2(ItemTemplate2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    user=anvil.users.get_user()
    if self.item['Current_user'] == 'None':
      #Not currently used
      self.stop_button.visible=False
      self.boot_button.visible=False
    else:
      if self.item['Current_user'] == user['email']:
        #Used by logged in user
        self.boot_button.visible=False
        self.use_button.visible=False
      else:
        #Used by another
        pass

  def set_state():
    pass
        

  def use_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    user=anvil.users.get_user()
    self.item['Current_user']=user['email']
    self.userNameLabel.text=self.item['Current_user']

  def stop_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.item['Current_user']='None'
    self.userNameLabel.text=self.item['Current_user']

  def boot_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    c = confirm("Are you sure you want to boot this user off? Please only do this if you've confirmed they're no longer using the PC!")
    # c will be True if the user clicked 'Yes'
    if c:
      self.stop_button_click()
