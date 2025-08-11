from ._anvil_designer import ItemTemplate2Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import datetime

TZ = datetime.timezone(datetime.timedelta(hours=0, minutes=0))

class ItemTemplate2(ItemTemplate2Template):
  def __init__(self, **properties):
    # Any code you write here will run before the form opens.
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.setup_the_row(**properties)

  def setup_the_row(self, **properties):
    self.refresh_data_bindings()
    
    self.set_state(self.item['Current_user'],True)
    if self.item['session_length'] is  None:
      self.item['session_length']=0

    #Check auto logoff times:
    logofftime=self.item['sesssion_start']+ datetime.timedelta(0,3600*self.item['session_length'])
    nowtime=datetime.datetime.now(TZ)
    #print(nowtime)
    #print(logofftime)
    if logofftime<nowtime:
      self.set_state('None')
    else:
      pass #don't logoff

  def set_state(self, name, start=False):
    '''Set the datbase and the form up for a particular named user (or "None" if no user)'''
    self.item['Current_user']=name

    if not start and name!='None':
      self.item['sesssion_start']=datetime.datetime.now(TZ)
      self.item['session_length']=float(get_open_form().hours_logoff.text)
    self.userNameLabel.text=self.item['Current_user']
    user=anvil.users.get_user()

    if self.item['Current_user'] == 'None':
      #Not currently used
      self.button.text="Use"
    else:
      if self.item['Current_user'] == user['email']:
        #Used by logged in user
        self.button.text="Stop"
      else:
        #Used by another
        self.button.text="Boot"


  def button_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.button.text == "Use":
      user=anvil.users.get_user()
      self.set_state(user['email'])
    elif self.button.text == "Stop":
      self.set_state('None')
    elif self.button.text == "Boot":
      c = confirm("Are you sure you want to boot this user off? Please only do this if you've confirmed they're no longer using the PC!")
      # c will be True if the user clicked 'Yes'
      if c:
        self.set_state('None')
    else:
      print("unknown button:"+self.button.text)

  def timer_1_tick(self, **event_args):
    """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
    self.setup_the_row()
        

