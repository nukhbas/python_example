def song():
    print("99 bottles of beer on the wall, 99 bottles of beer")
    for i in range(99)[::-1]:
        print("Take one down, pass it around," + str(i) + "bottles of beer on the wall.")
song()        