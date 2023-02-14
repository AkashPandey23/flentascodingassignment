t = int(input())
for _ in range(t):
    str1 = input()
    str2 = input()
    if str1 in str2 or str1[::-1] in str2:
        print("YES")
    else:
        print("NO")
