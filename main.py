# CC BY (c) Jesse Ceulemans 2023

import datetime
import os
import pymongo
import json

# Source: https://www.digitalocean.com/community/tutorials/read-large-text-files-in-python
dbname = "huwebshop"
column_name = "sessions"

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient[dbname]
mycol = mydb[column_name]
file_name = "sessions_modified.json"

# If you want to overwrite uncomment the following
#mycol.delete_many({})

print(f'File Size is {os.stat(file_name).st_size / (1024 * 1024)} MB')

txt_file = open(file_name)

count = 0
timestart = datetime.datetime.now()

for line in txt_file:
    # we can process file line by line here, for simplicity I am taking count of lines
    count += 1
    try:
        x = mycol.insert_one(json.loads(line))
    except:
        print(f'error detected at: {count}:\n\t*{line}')

    if count % 10000 == 0:
        print(round(count / (10 ** 6), 2), 'Million |', round((datetime.datetime.now() - timestart).total_seconds(), 1), 's')

txt_file.close()

print(f'Number of Lines in the file is {count}')
