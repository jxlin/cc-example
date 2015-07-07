# example of program that calculates the median number of unique words per tweet.
import statistics   # used for the function median
import string       # used to manipulate strings
import glob         # used to get the file paths from the input directory
import ntpath       # used to get the absolute file name
from   operator import itemgetter # used to make operation on list
import sys
import os

# getting the input directory from the command args
input=str(sys.argv[1])
# getting the output file name from the command args
output=str(sys.argv[2])
if not os.path.exists(output.split('/')[1]):
   os.mkdir(output.split('/')[1])
# get the file paths from the input directory
files=glob.glob(input)
#define a list to store the paris (filename, filepath)
filenames=[]

for filepath in files:
   # store the file name ,filepath in the list
   # after convert the filenames to lowercase
   filenames.append(((ntpath.basename(filepath)).lower(),filepath))
   # sort the list based on the file names 
   filenames=sorted(filenames,key=itemgetter(0))
   # get the first element from the list which contains the sorted actual file name
   files= [x[1] for x in filenames]

# define a list to store the number of words
num_words = []
# define a median_values list using num_lines as index
num_lines = 0
median_values={}

# parse all the files in the directory alphabatically
for file in files:
     # open each file for read only access
     with open(file, 'r') as f:
         for line in f:
            words = line.split()
            num_lines+=1
            # store the number of words per line in the list num_words
            num_words.append(len(words))
            #calculate the median value for the n.words in the current line
            # with the previous lines
            median_values[num_lines]=statistics.median(num_words)

# open the ft2 text file in write access mode
with open (output, 'w') as fout:
    # write each  median value in float format per each line 
    for i in range(1,num_lines+1):
        fout.write (str(float(median_values[i])) + "\n")
