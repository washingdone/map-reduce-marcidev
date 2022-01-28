fi = open("sortedData.txt","r")
fo = open("outputData.txt", "w")

thisKey = ""
thisValue = 0.0

for line in fi:
  data = line.strip().split('\t')
  store, amount = data
  if store != thisKey:
    if thisKey:

      # output the last key value pair result
      fo.write(thisKey + '\t' + str(thisValue)+'\n')

    # start over when changing keys
    thisKey = store
    thisValue = 0.0

  # apply the aggregation function
  thisValue += float(amount)

# output the final entry when done
fo.write(thisKey + '\t' + str(thisValue)+'\n')

fi.close()
fo.close()