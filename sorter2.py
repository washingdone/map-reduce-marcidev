# Author: Marci DeVaughan
# Created: 29 Jan 2022
# Updated: 29 Jan 2022
# A simple sort program

fi = open("remappedData.txt","r")  # open file, read-only
fo = open("finalData.txt", "w") # open file, write
lines = fi.readlines()
lines.sort(reverse=True) # sort in descending order

for line in lines:
	fo.write(line)
fi.close()
fo.close()
