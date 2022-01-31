# Author: Marci DeVaughan
# Created: 29 Jan 2022
# Updated: 30 Jan 2022
# A simple map reduce program

fi = open("outputData.txt","r")  # open file, read-only
fo = open("remappedData.txt", "w") # open file, write
for line in fi:  
    rowData = line.strip().split("\t") # DT: List of Lists
    if len(rowData) == 2:
        location, amount = rowData #assign names
        splitArr = amount.split(".",1) # split in two for trimming
        splitArr[0] = splitArr[0].zfill(4) # pad the dollars side to 4 characters
        splitArr[1] = splitArr[1][:2] # trim the cents side to 2 characters
        formatAmount = splitArr[0]+"."+splitArr[1] # combine the reformatted parts back into proper format
        fo.write(f"{formatAmount}\t{location}\n")
fi.close()
fo.close()