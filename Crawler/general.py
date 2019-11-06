import os


# Each website is a separate project (folder)
def create_project_dir(directory):
	if not os.path.exists(directory):
		print('Creating Project Directory ' + directory)
		os.makedirs(directory)
		#db_dir = directory + '/Database'
		#print('Crating Database directory ' + db_dir)
		#os.makedirs(db_dir)		
		
# create_project_dir('nintendo')

## create queue and crawled files (if note exists)        
def create_data_files(project_name, base_url):
    queue = os.path.join(project_name , 'queue.txt')
    crawled = os.path.join(project_name,'crawled.txt')
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')
        
        
# Create a new file
def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)

    
# Add data onto an existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')
        

# Delete the contents of a file
def delete_file_contents(path):
    open(path, 'w').close()
    
    
# Read a file and convert each line to set items
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results


# Iterate through a set, each item will be a line in a file
def set_to_file(links, file_name):
    with open(file_name,"w") as f:
        for line in sorted(links):
            f.write(line+"\n")