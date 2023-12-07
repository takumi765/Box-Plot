import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import font_manager

# 日本語フォントの設定
font_path = "C:/Windows/Fonts/meiryo.ttc"  # ご利用の環境に合わせてフォントパスを指定してください
jp_font = font_manager.FontProperties(fname=font_path).get_name()
plt.rcParams['font.family'] = jp_font

title = "hogehoge"

# CSVファイルからデータを読み込む
# df = pd.read_csv('./multimodal/IPQ-'+title+'.csv')
df = pd.read_csv('./fugafuga/'+title+'.csv')

# 被験者ID以外の列を条件として整形
condition_columns = df.columns[1:]  # 被験者ID以外の列を条件とする
df_long = pd.melt(df, id_vars='subject', value_vars=condition_columns, var_name='Condition', value_name='Value')

# 箱ひげ図を描画
plt.figure(figsize=(5, 6))
sns.boxplot(x='Condition', y='Value', data=df_long)
# plt.title('IPQ-'+title, fontsize=20)
plt.xlabel('条件', fontsize=14)
plt.ylabel('スコア', fontsize=14)

# x軸のラベルを斜めにする
plt.xticks(rotation=45, ha='right',fontsize=12)
# y軸の範囲を設定
plt.ylim(-10, 10)
# y軸の目盛りのフォントサイズを指定
plt.yticks(fontsize=12)
# レイアウトを調整
plt.tight_layout()

# PDFとして保存
plt.savefig('./pdf/boxplot-'+title+'.pdf', format='pdf')

plt.show()
