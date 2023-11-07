# その3
a = list(range(0, 10))
print(a)
# # 問1
print(a[0])

# 問2
a.pop()
print(a)

# 問3
# 先頭
print(a[0])

# 中間
half = len(a) // 2
if len(a) % 2:
    print(a[half])
else:
    print(a[half], a[half + 1])

# 最後尾
print(a[-1])