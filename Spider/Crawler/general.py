import os


# Each website is a separate project (folder)
def create_project_dir(directory):
    if not os.path.exists('Projects'):
        print('Creating Projects Directory with Name :' + 'Projects')
        os.makedirs('Projects')
        
        # Create Directories for Project Name
        if not os.path.exists('Projects/' + directory):
            print('Creating New Project Directory ' + 'Projects/' + directory)
            os.makedirs('Projects/' + directory)
        
        # Create Directiories for Project Crawler task Details
        if not os.path.exists('Projects/' + directory+'/Task'):
            print('Creating New Project Task Directory ' + 'Projects/' + directory + '/Task')
            os.makedirs('Projects/' + directory + '/Task')

        # create Dirctories for Scraped Data
        if not os.path.exists(directory+'/Data'):
            print('Creating Project Data Directory ' + 'Projects/' + directory + '/Data')
            os.makedirs('Projects/' + directory+'/Data')

        # Create Directories for Database
        if not os.path.exists('Projects/' + directory + '/Database'):
            print('Creating DataBase Directories : ' + 'Projects/' + directory + '/Database')
            os.makedirs('Projects/' + directory + '/Database')

            # MySQL Database Directory
            # if not os.path.exists('Projects/' + directory + '/Database' + '/MySQL'):
                # os.makedirs('Projects/' + directory + '/Database' + '/MySQL')

            # SQLite Database Directory
            if not os.path.exists('Projects/' + directory + '/Database' + '/SQLite'):
                os.makedirs('Projects/' + directory + '/Database' + '/SQLite')

            # Postgres Database Directory
            # if not os.path.exists('Projects/' + directory + '/Database' + '/PostGreSQL'):
                # os.makedirs('Projects/' + directory + '/Database' + '/PostGreSQL')

            # Oracle Database Directory
            # if not os.path.exists('Projects/' + directory + '/Database' + '/Oracle'):
                # os.makedirs('Projects/' + directory + '/Database' + '/Oracle')

            # MongoDB Database Directory
            # if not os.path.exists('Projects/' + directory + '/Database' + '/MongoDB'):
                # os.makedirs('Projects/' + directory + '/Database' + '/MongoDB')
        

# create queue and crawled files for Crawler and Scraper (if note exists)
def create_task_files(project_name, base_url):
    queue = os.path.join('Projects/' + project_name +'/Task', 'queue.txt')
    crawled = os.path.join('Projects/' + project_name + '/Task', 'crawled.txt')
    scraper_queue = os.path.join('Projects/' + project_name + '/Task', 'scraper_queue.txt')
    scraped = os.path.join('Projects/' + project_name + '/Task', 'scraped.txt')
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')
    if not os.path.isfile(scraper_queue):
        write_file(scraper_queue, '')
    if not os.path.isfile(scraped):
        write_file(scraped, '')


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
    with open(file_name, "w") as f:
        for line in sorted(links):
            f.write(line + "\n")
