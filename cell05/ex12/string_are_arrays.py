import sys

if len(sys.argv) != 2:
    print("none")
else:
    text = sys.argv[1]
    count = 0
    for char in text:
        if char == 'z':
            count += 1
    if count == 0:
        print("none")
    else:
        print("z" * count)
