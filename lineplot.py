import pandas as pd
import matplotlib.pyplot as plt

def plot_number_line_from_csv(file_path, x_column, output_path):
    # CSVファイルを読み込む
    df = pd.read_csv(file_path)

    # 数直線上にプロット
    plt.axhline(0, color='black', linewidth=1.0)
    plt.yticks([])

    values = list(df[x_column])
    plt.scatter(values, [0]*len(values), color='red', s=100) #  数値を赤い点でプロット sは赤い点のサイズ

    # PDF形式で保存
    plt.savefig(output_path, format='pdf')

    plt.show()

# 例: CSVファイル 'data.csv' から 'value' 列を読み込んでプロット
plot_number_line_from_csv('./paired/exp.csv', 'value', './pdf/exp.pdf')
