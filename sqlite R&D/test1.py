import sqlite3 
class SqliteHelper:
	def __init__(self,name=None):
		self.conn = None
		self.cursor = None
		
		if name:
			self.open(name)

	def open(self, name):
		try:
			self.conn = sqlite3.connect(name)
			self.cursor = self.conn.cursor()
			print(sqlite3.Version)
		except sqlite3.Error as e:
			print("failed connecting to database...")
			
test = SqliteHelper("")