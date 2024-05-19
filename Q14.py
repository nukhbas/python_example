
listOfWords = ['bounty','twist','sneaker','mars','milka']
 
listOfInts = []
 
x = range(len(listOfWords)) 
for i in x:
    listOfInts.append(len(listOfWords[i]))
 
print ("List of words:"+str(listOfWords))    
print ("List of wordlength:"+str(listOfInts))
