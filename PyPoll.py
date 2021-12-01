#    The data we need to retrieve
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Percentage of votes each candidate won
# 4. Total number of votes each candidate won
# 5. The winner of the election based on popular vote

import csv
import os

# Assign a variable for the file to load and the path.
# file_to_load = 'Resources/election_results.csv'

# # Open the election results and read the file.
# election_data = open(file_to_load, 'r')

# # To do: perform analysis.

# # Close the file.
# election_data.close()

# # Open the election results and read the file
# with open(file_to_load) as election_data:

#      # To do: perform analysis.
#      print(election_data)
# Add our dependencies.


# # Assign a variable for the file to load and the path.
# file_to_load = os.path.join("Resources", "election_results.csv")
# # Open the election results and read the file.
# with open(file_to_load) as election_data:

#     # Print the file object.
#      print(election_data)

# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("Analysis", "election_analysis.txt")
# # Use the open statement to open the file as a text file.
# outfile = open(file_to_save, "w")
# # Write some data to the file.
# outfile.write("Hello World")

# # Close the file
# outfile.close()
# # example
# Create a filename variable to a direct or indirect path to the file.
# # file_to_save = os.path.join("analysis", "election_analysis.txt")
#
# Using the with statement open the file as a text file.
# #with open(file_to_save, "w") as txt_file:

# Write some data to the file.
#      txt_file.write("Hello World")
# Write three counties to the file.
#      txt_file.write("Arapahoe, ")
#      txt_file.write("Denver, ")
#      txt_file.write("Jefferson")

# drill question
#       txt_file.write("{:s}\n{:s}\n".format("Counties in the Election", len("Counties in the Election") * "-"))
#       txt_file.write("Counties in the Election\n)

#       Write three counties to the file.
# #     txt_file.write("Arapahoe\nDenver\nJefferson")


# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data) 
    # Print each row in the CSV file.
# for row in file_reader:
#     print(row)
# Read and print the header row.
    headers = next(file_reader)
    print(headers)
