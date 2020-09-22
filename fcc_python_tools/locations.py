import os
repo = os.getenv('ANAROOT')

class loc : pass
loc.ROOT = repo+'/'
loc.OUT = repo+'output/'
loc.DATA = loc.ROOT+'data'
loc.PLOTS = loc.OUT+'plots'
loc.TABLES = loc.OUT+'tables'
loc.JSON = loc.OUT+'json'
