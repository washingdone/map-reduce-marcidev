# Author: Marci DeVaughan
# Created: 29 Jan 2022
# Updated: 29 Jan 2022
# A simple map reduce program

fi = open("outputData.txt","r")  # open file, read-only
fo = open("remappedData.txt", "w") # open file, write
for line in fi:  
    rowData = line.strip().split("\t") # DT: List of Lists
    if len(rowData) == 2:
        location, amount = rowData #assign names
        fo.write("{0}\t{1}\n".format(amount, location))
fi.close()
fo.close()