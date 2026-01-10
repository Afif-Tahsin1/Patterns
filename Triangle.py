print("Half pyramids patterns of stars (*):")
n = int(input("Input the numbers of row: "))
for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print()
