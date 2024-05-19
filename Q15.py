def longestLength(ch):
    max1 = len(ch[0])
    arr = ch[0]
 
   
    for i in ch:
        if(len(i) > max1):
 
            max1 = len(i)
            arr = i
 
    print("longest word:", arr)
    print("its length:", max1)
    
longestLength(["bounty", "twister", "milka", "galaxy"])
    
    