import numpy as np


random_cutting=[]
for i in range(30):
    # 行と列のサイズをランダムに設定
    rows = np.random.randint(1, 11)  # 1から10までのランダムな行数
    cols = np.random.randint(1, 11)  # 1から10までのランダムな列数

    # ランダムに0と1を選択して2次元配列を作成
    array = np.random.randint(2, size=(rows, cols))

    random_cutting.append(array)

print(random_cutting)