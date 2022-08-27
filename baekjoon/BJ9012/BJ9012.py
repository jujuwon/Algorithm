import sys

T = int(sys.stdin.readline())

ps_list = []

for i in range(T):
    ps = sys.stdin.readline().strip()
    flag = True
    ps_list.clear()
    for j in range(len(ps)):
        if ps[j] == "(":
            ps_list.append("(")
        else:
            if ps_list:
                ps_list.pop()
            else:
                flag = False
                break
    if flag and (not ps_list):
        print("YES")
    else:
        print("NO")