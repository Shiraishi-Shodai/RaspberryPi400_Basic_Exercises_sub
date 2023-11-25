def even_numbers(n):
    for i in range(n):
        print(f'this {i}')
        
        if i % 2 == 0:
            yield i

# ジェネレーターを使って偶数を取得
gen = even_numbers(10)
print(gen)
for num in gen:
    print(num)
