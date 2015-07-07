# example of program that calculates the total number of times each word has been tweeted.
import string
import glob  # used for reading files from specific path
import sys   # used to read command arg 

# get the input directory tweet_input that contain text files
input=str(sys.argv[1])
# get the output file path tweet_output
output=str(sys.argv[2])
# get the file paths from the input directory
files=glob.glob(input)
# define a dictionary to store the word and the number of occurences 
wordcount = {}
# parse all the files in the directory
for file in files:
    # open each file for read only access
    with open(file, 'r') as f:
        # for each line in the txt file
        for line in f:
            # convert all the letters to a lower case and retrieve the words per line 
            words = line.lower().split()
            # for each word check if already occured or not and count the no. of occurences
            for word in words:
                wordcount[word] = wordcount.get(word, 0) + 1
# open the tweet_output text file in write access mode
with open (output, 'w') as fout:
   # write  the words and number of occurences to the output file 
   for word in sorted(wordcount):
      fout.write(word +"\t" +str(wordcount[word])+ "\n")