# Author: Marci DeVaughan
# Created: 28 Jan 2022
# Updated: 28 Jan 2022
# A simple map reduce program

fi = open("mappedData.txt","r")  # open file, read-only
fo = open("sortedData.txt", "w") # open file, write
lines = fi.readlines()
lines.sort()

for line in lines:
	fo.write(line)
fi.close()
fo.close()
