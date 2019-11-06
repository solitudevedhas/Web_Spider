import os
import sqlite3

class SqliteHelper:
			
	def __init__(self,name=None):
		self.conn = None
		self.cursor = None
		
		if name:
			if not os.path.exists('Database'):
				os.makedirs('Database')
				self.open('Database/'+name)
	
	def open(self, name):
		try:
			self.conn = sqlite3.connect('Database/'+ name)
			self.cursor = self.conn.cursor()
			print(sqlite3.version)
		except sqlite3.Error as e:
			print("Failed connecting to Database...")
	

test = SqliteHelper('test.db')
