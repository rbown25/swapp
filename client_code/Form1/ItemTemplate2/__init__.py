from ._anvil_designer import ItemTemplate2Template
from anvil import *
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import datetime

class ItemTemplate2(ItemTemplate2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.set_state(self.item['Current_user'],True)


  def set_state(self, name, start=False):
    '''Set the datbase and the form up for a particular named user (or "None" if no user)'''
    self.item['Current_user']=name
    if not start:
      self.item['sesssion_start']=datetime.datetime.now()
    self.userNameLabel.text=self.item['Current_user']
    user=anvil.users.get_user()

    if self.item['Current_user'] == 'None':
      #Not currently used
      self.stop_button.visible=False
      self.boot_button.visible=False
      self.use_button.visible=True
    else:
      if self.item['Current_user'] == user['email']:
        #Used by logged in user
        self.stop_button.visible=True
        self.boot_button.visible=False
        self.use_button.visible=False
      else:
        #Used by another
        self.stop_button.visible=False
        self.boot_button.visible=True
        self.use_button.visible=False
        

  def use_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    user=anvil.users.get_user()
    self.set_state(user['email'])

  def stop_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.set_state('None')

  def boot_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    c = confirm("Are you sure you want to boot this user off? Please only do this if you've confirmed they're no longer using the PC!")
    # c will be True if the user clicked 'Yes'
    if c:
      self.set_state('None')
