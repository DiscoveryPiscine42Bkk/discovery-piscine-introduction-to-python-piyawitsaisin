import sys

if len(sys.argv) == 1:
    print("none")
else:
    args = sys.argv[1:]  
    print(f"parameters: {len(args)}")
    for arg in args:
        print(f"{arg}: {len(arg)}")
