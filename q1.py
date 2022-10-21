def removechar(c, s):
    n = ""
    c = str(c)
    for i in s:
        if i == c:
            pass
        else:
            n+=i
    return n





print(removechar(",", "First,Last 30,12,24"))
