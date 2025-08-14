i=int(input("Enter the number of rows: "))
for row in range(i+1):
    ascit=65
    for col in range(row):
        print(chr(ascit), end=' ')
        ascit += 1
    print()
