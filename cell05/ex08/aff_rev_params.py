import sys
if len(sys.argv) < 2:
    print("none")
else:
    for age in reversed(sys.argv[1:]):
        print(age)