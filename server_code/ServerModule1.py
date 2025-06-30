import anvil.files
from anvil.files import data_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import csv

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
@anvil.server.callable
def import_new_users():
  '''This function will import any new users in the csv file "innovians.csv" to the Users table.
  It is intended to be run via the server REPL. To do this type:
  anvil.server.call('import_new_users')'''
  all_staff=[]
  current_staff=[]
  file = open(data_files['innovians.csv'], "rU")
  reader = csv.reader(file, delimiter=',')
  for row in reader:
    all_staff.append(row[0])
  #text = file.read()
  for row in app_tables.users.search():
    current_staff.append(row["email"])
  staff_to_add=list(set(all_staff).difference(current_staff))

  for person in staff_to_add:
    row = app_tables.users.add_row(email=person,enabled=True)
    print(row['email'])