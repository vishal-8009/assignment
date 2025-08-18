n=int(input("Enter a Row:"))
for row in range(n):
    for col in range(1,(n-row+1)):
        print(chr(col+64), end="")
    for col in range(1,row+1):
        print(" ", end="") 
    for col in range(2,row+1):
            print(" ", end="")
    for col in range(n-row,0,-1):
        if col==n:
            continue
        print(chr(col+64),end="")
     print()
        