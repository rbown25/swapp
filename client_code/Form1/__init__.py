from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server
import anvil.http

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    anvil.users.login_with_form()

    self.PC_list.items = app_tables.pcs.search()

    #Joke
    resp = anvil.http.request(url="https://icanhazdadjoke.com/",
                              method="GET",
                              json=True,
                              headers= {
                                "User-Agent": "In-house app, rich.bown@innoviatech.com",
                                "Accept": "application/json"
                              })
    self.joke_text.text=resp['joke']
