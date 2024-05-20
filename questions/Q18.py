def pangram(ch):
    letters = ['a','b', 'c', 'd', 'e','f', 'g', 'h', 'i','j', 'k',\
           'l', 'm','n', 'o', 'p', 'q','r', 's', 't', 'u','v', 'w', 'x', 'y','z' ]
    i = 0
    
    if i in letters and i in str:
        print("its a pangram")
    else:
        print("its not a pangram")
 
ch = "The quick brown fox jumps over the lazy dog"       

pangram(ch)          