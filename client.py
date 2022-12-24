import rpyc
from constRPYC import * #-

class Client:
  conn = rpyc.connect(SERVER, PORT) # Connect to the server
  print(f"values = {conn.root.exposed_value()}")
  print("adding 5")
  conn.root.exposed_append(5)       # Call an exposed operation,
  print("adding 6")                 # and append two elements
  conn.root.exposed_append(6)
  print(f"values = {conn.root.exposed_value()}")     # Print the result
  print ("removing 5")
  conn.root.exposed_remove(5)
  print(f"values = {conn.root.exposed_value()}")     # Print the result
  print(f"searching for '5'")
  print(f"index of '5': {conn.root.exposed_index_of(5)}")
  print(f"searching for '6'")
  print(f"index of '6': {conn.root.exposed_index_of(6)}")
  print("adding 3")                 # and append two elements
  conn.root.exposed_append(3)
  print(f"values = {conn.root.exposed_value()}")     # Print the result
  print(f"sort values")
  conn.root.exposed_sort()
  print(f"values = {conn.root.exposed_value()}")     # Print the result
  print(f"clear values")
  conn.root.exposed_clear()
  print(f"values = {conn.root.exposed_value()}")     # Print the result

