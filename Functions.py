import matplotlib.pyplot as plt
import numpy as np


def plotSCA(data_X):
    """
    1次元データの散布図をプロットする関数

    :param data: 1次元データ(リストまたは配列)
    SCAは次の形で関数に入ってくる(要素数は99)
    SCA = np.zeros((99, 1), float)
    """

    # フィギュアを作成し、サイズを設定（縦横比1：2）
    plt.figure(figsize=(3, 6))

    # Xのデータを準備
    data_Y = np.linspace(0, 1, 99)

    # 背景に白黒のグラデーションを描画
    gradient = np.linspace(0, 1, 100).reshape(1, -1)
    plt.imshow(np.vstack((gradient, gradient)),
               cmap='gray',
               extent=[-1, 1, 0, 1],
               aspect='auto',
               alpha=0.2)

    # 散布図をプロット
    # plt.scatter(data, range(len(data)),)
    # plt.scatter(data[0], data[1])
    # plt.plot(data[0], data[1], marker='o', linestyle='-')
    plt.plot(data_X, data_Y, marker='o', linestyle='-')

    # グリッドを有効にする
    plt.grid(True)

    # グラフのタイトルと軸ラベルを設定
    plt.title("SCA")
    plt.xlabel("Z-axis")
    plt.ylabel("Pupil")

    # グラフを表示
    plt.show()


# テスト用のデータ

data_X = np.flip([-0.449887435,
                 -0.495653416,
                 -0.474286688,
                 -0.413830312,
                 -0.333848974,
                 -0.248263825,
                 -0.167080029,
                 -0.097470406,
                 -0.044466717,
                 -0.011400109,
                 0])
# 要素数を99に拡張
data_X = np.interp(np.linspace(0, 1, 99),
                   np.linspace(0, 1, len(data_X)),
                   data_X)


# 関数をテスト
if __name__ == "__main__":
    plotSCA(data_X)
