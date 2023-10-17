"""
Your module description
"""
import os
import time
import datetime

# Change the current working directory
directory = os.chdir('gold-oct-2023')

# Get the current working directory
current_directory = os.getcwd()

# List all files in the working directory
files = os.listdir(current_directory)

# Import datetime
dt = datetime.datetime

# List of dictionaries for storing file information
file_list = []
count = 0

# Iterate over each file in the directory
for file in files:
    count = count + 1
    # Get the creation time of the file
    timestamp = os.path.getctime(file)
    # Convert the timestamp to a human-readable date and time format
    date_time = dt.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')  # with help from a little Google search
    # Create a dictionary for each file containing relevant information
    file_info = {
        "index:": count,
        "file_name": file,
        "file_size": os.path.getsize(file),
        "file_time": date_time
        
    }
    # Append the file information dictionary to the list
    file_list.append(file_info)

# Print the list of dictionaries
for file_info in file_list:
    print(file_info)