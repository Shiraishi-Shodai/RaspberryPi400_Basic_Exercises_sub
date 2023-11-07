
try:
    num = int(input("数字を入力してください"))
    
    if num == 0:
        print(f'{num} はゼロです')
    elif num < 0:
        print(f'{num} は負の数です')
    else:
        print(f'{num} は正の数です')
        
    
except ValueError:
    print("数字以外が入力されました")

# import re
# num = input("数字を入力してください")
# if re.match(r'\d+', num):
#     num = int(num)
#     print(type(num))
# else:
#     print('みすまっち')