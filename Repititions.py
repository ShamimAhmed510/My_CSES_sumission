s = input().strip()

ans = 1
cnt = 1

for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 1

ans = max(ans, cnt)

print(ans)
