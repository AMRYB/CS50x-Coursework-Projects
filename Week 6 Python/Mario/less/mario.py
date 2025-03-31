while True:
    try:
        height = int(input("Height: "))
        if 1 <= height <= 8:
            break
    except:
        print("", end="")

for j in range(height):
    for _ in range(height - j - 1):
        print(" ", end="")

    for i in range(j + 1):
        print("#", end="")

    print()
