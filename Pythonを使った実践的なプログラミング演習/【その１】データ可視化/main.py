
# 描画結果を画像として表示
# import matplotlib as mpl
# mpl.use('Agg')

import matplotlib.pyplot as plt
import pandas as pd
import japanize_matplotlib

x = list(range(10))
y = list(range(10))

plt.scatter(x, y)
plt.title("タイトル")
plt.show()

# plt.savefig('./ret.png')