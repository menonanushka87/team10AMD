import json
import re
from datetime import datetime
import os


def collect_file_paths():
    """
    Prompt the user to input file paths and collect them in a list.
    Continues asking for more paths until the user decides to stop.
    """
    file_paths = []
    while True:
        file_path = input("Please enter a file path, or type 'done' to finish: ")
        if file_path.lower() == 'done':
            break
        if os.path.isfile(file_path):  # Verify that the file exists
            file_paths.append(file_path)
        else:
            print("File does not exist. Please try again.")
    return file_paths

def extract_commit_info(file_paths, default_author):
   
    # Get the current date and format it as YYYY-MM-DD
    current_date = datetime.now().strftime("%Y-%m-%d")


    authors = ["tensorflower-gardener", "golechwierowicz", "fchollet", "fwcore", "golechwierowicz", default_author]
    timestamps = ["Aug 2, 2019", "Jan 3, 2020", "Apr 11, 2017", "Jan 11, 2024", "Jun 7, 2024", current_date]
    results = []

    # Define the baseline file and author explicitly
    baseline_file = "database-b8b8ebcf851d-2017-04-11.sarif"
    baseline_author = authors[3]  # This is the third author in our list
    baseline_timestamp = timestamps[2]

    # Look at each file
    for index, file_path in enumerate(file_paths):
        # Check if the file is the baseline file
        if baseline_file in file_path:
            author = baseline_author
        elif index < len(authors):
            author = authors[index]
        else:
            author = default_author  # Use the user's input name as the default author
            timestamps = current_date
        
        # Extract timestamp in the file name using a pattern search
        timestamp_match = re.search(r'\d{4}-\d{2}-\d{2}', file_path)
        timestamp = timestamp_match.group(0) if timestamp_match else "Unknown timestamp"
        
        # Compare this author to the baseline author
        if author == baseline_author:
            status = "Same Author from baseline"
        else:
            status = "Unique Author"

        # Save information about this file
        results.append({
            "file_path": file_path,
            "author": author,
            "timestamp": timestamp, #date from file
            "commit date": timestamps[index], #commit time from tensorflow
            "process_date": current_date,  # Add the current date to each result
            "status": status
        })

    return results

# Example usage with user input for the default author:
default_author = input("Please enter your name: ")
file_paths = [
    "database-da5091bf507b-2019-08-02.sarif",
    "database-d25dd807485c-2020-01-03.sarif",
    "database-b8b8ebcf851d-2017-04-11.sarif",
    "database-5a7786812dd4-2024-01-11.sarif",
    "database-a632c89dd778-2024-06-07.sarif",
]

# Printing the results to see them
results = extract_commit_info(file_paths, default_author)
for result in results:
    print(result)
    print()  # Add a new line after each result

