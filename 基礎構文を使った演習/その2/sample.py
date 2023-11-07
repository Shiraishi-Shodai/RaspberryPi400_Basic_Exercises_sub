# 問1
print("Hello " + "World")

# 問2
print("one", "two", "three")

# 問3
text = "Hello world!"
# スライス
print(text[-6:])
# reモジュール(末尾がworld!で終わる文字列を抽出)
import re
print(re.findall("world!$", text)[0])

m = re.search("world!$", text)
print(m.group())