import matplotlib.pyplot as plt


# plotSCAの仕様
# 2次元配列とする（x, y）の形で情報を持つ事
def plotSCA(data):
    """
    1次元データの散布図をプロットする関数

    :param data: 1次元データ（リストまたは配列）
    """

    # 散布図をプロット
    # plt.scatter(data, range(len(data)),)
    # plt.scatter(data[0], data[1])
    plt.plot(data[0], data[1], marker='o', linestyle='-')

    # グリッドを有効にする
    plt.grid(True)

    # グラフのタイトルと軸ラベルを設定
    plt.title("SCA")
    plt.xlabel("Z-axis")
    plt.ylabel("Pupil")

    # グラフを表示
    plt.show()


# テスト用のデータ
data = [[-0.449887435,
        -0.495653416,
        -0.474286688,
        -0.413830312,
        -0.333848974,
        -0.248263825,
        -0.167080029,
        -0.097470406,
        -0.044466717,
        -0.011400109,
        0],
        [1.0,
        0.9,
        0.8,
        0.7,
        0.6,
        0.5,
        0.4,
        0.3,
        0.2,
        0.1,
        0]]

# 関数をテスト
if __name__ == "__main__":
    plotSCA(data)
