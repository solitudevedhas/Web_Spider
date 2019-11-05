import os

## Each website crawl is a seprate project

def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating Project ' + directory)
        os.makedirs(directory)
        
# create_project_dir('nintendo')

## create queue and crawled files (if note exists)
def create_data_files(project_name,base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled_txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')
        

## craete a new file 
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()
    
create_data_files('nintendo','https://www.nintendo.com/')