def findlarge(l):
    if len(l)<4:
        print("Error")
    else:
        l=l[::-1]=list(set(sorted(l)))
        print("Second largest {}\nFourth Largest {}".format(l[1],l[3]))
findlarge([1,2,3,54,56,75,3,5])
