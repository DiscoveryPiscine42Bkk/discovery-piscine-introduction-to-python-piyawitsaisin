import sys

if len(sys.argv) < 2:
    print("none")
else:
    found = False
    for word in sys.argv[1:]:
        if not word.endswith("ism"):
            print(word + "ism")
            found = True
    if not found:
        print("none")
