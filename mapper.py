# Author: Marci DeVaughan
# Created: 26 Jan 2022
# Updated: 28 Jan 2022
# A simple map reduce program

fi = open("inputData.txt","r")  # open file, read-only
fo = open("mappedData.txt", "w") # open file, write
for line in fi:  
    rowData = line.strip().split("    ") # DT: List of Lists
    # print (rowData )
    # print (len(rowData))
    if len(rowData) == 6:
        date, time, location, dept, amount, payType = rowData
        #assign names
        # print ("{0}\t{1}".format(location, amount))
        fo.write("{0}\t{1}\n".format(location, amount))
fi.close()
fo.close()