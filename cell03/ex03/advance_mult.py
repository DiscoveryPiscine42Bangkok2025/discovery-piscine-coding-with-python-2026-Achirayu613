import sys
if len(sys.argv) > 1:
    print("none")
else:
    i = 0
    while i <= 10:
        j = 0
        print(f"Table de {str(i)} : ",end = "")
        while j <= 10:
            mult = i * j
            if j != 10:
                print(str(mult), " ", end="")
            else:
                print(str(mult))
            j += 1
        i += 1