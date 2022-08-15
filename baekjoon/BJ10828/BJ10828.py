import sys

N = int(sys.stdin.readline())

stack = []

for i in range(N):
    cmd = sys.stdin.readline().strip()
    if cmd == "pop":
        if stack:
            print(stack[-1])
            stack.pop()
        else:
            print("-1")
    elif cmd == "size":
        print(len(stack))
    elif cmd == "empty":
        if stack:
            print("0")
        else:
            print("1")
            
    elif cmd == "top":
        if stack:
            print(stack[-1])
        else:
            print("-1")
    else:
        stack.append(cmd.split()[1])