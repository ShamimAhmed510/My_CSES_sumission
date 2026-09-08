s = input()
p = input()

lps = [0] * len(p)
j = 0
for i in range(1, len(p)):
    while j and p[i] != p[j]:
        j = lps[j - 1]
    if p[i] == p[j]:
        j += 1
        lps[i] = j

j = ans = 0
for c in s:
    while j and c != p[j]:
        j = lps[j - 1]
    if c == p[j]:
        j += 1
        if j == len(p):
            ans += 1
            j = lps[j - 1]

print(ans)
