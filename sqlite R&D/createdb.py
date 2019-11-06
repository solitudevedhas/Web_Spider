import os
import sqlite3
from sqlite3 import Error

		
def create_project_dir(directory):
	if not os.path.exists(directory):
		print('Creating Project Directory ' + directory)
		os.makedirs(directory)
		db_dir = directory + '/Database'
		print('Crating Database directory ' + db_dir)
		os.makedirs(db_dir)
		
create_project_dir('nintendo')



