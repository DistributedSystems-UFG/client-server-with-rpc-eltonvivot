import rpyc
from constRPYC import * #-
from rpyc.utils.server import ThreadedServer

class DBList(rpyc.Service):
  value = []

  def exposed_append(self, data):
    self.value = self.value + [data]
    return self.value

  def exposed_value(self):
    return self.value

  def exposed_sort(self):
    return self.value.sort()
  
  def exposed_clear(self):
    return self.value.clear()
  
  def exposed_index_of(self, data):
    return None if not data in self.value else self.value.index(data)
  
  def exposed_remove(self, data):
    if not data in self.value: return f"'{data}' not in values"
    self.value.remove(data)
    return self.value

if __name__ == "__main__":
  server = ThreadedServer(DBList(), port = PORT)
  server.start()

