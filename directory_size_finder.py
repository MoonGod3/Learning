# Solution to programming challenge for Learning Python course
# LinkedIn Learning Python course by Joe Marini modified by CE for learning purposes only!
#

import os
import shutil

totalbytes = 0
folder = "deps"

# get a list of all the files in the current directory
dirlist = os.listdir()

#for fun, print the list of files
print(dirlist)

for entry in dirlist:
    # make sure it's a file!
    if os.path.isfile(entry) and (entry.endswith(".txt")):
        # add the file size to the total
        filesize = os.path.getsize(entry)
        totalbytes += filesize
print("The total size of all files in Ch3 - Files is:", totalbytes)


# # create a subdirectory called "results" if it doesn't exist
# path2 = r"C:\\Users\mpcha\\My Learning\\Python\\LinkedInLearning-learning-python-2896241-3812f50\\Ch3 - Files\\results"
# if os.path.isdir(path2) is True:
#     shutil.rmtree("results")

# ###Now create the subdirectory
# os.mkdir("results")

# # # create the output file
# resultsfile = open("results/results.txt", "w+")
# if resultsfile.mode == "w+":
#     resultsfile.write("Total bytecount:" + str(totalbytes) + "\n")
#     resultsfile.write("Files list:\n")
#     resultsfile.write("--------------\n")
#     # write the results into the file
#     for entry in dirlist:
#         if os.path.isfile(entry):
#             # write the file name to the results ledger
#             resultsfile.write(entry + "\n")

#     # close the file when done
#     resultsfile.close()
