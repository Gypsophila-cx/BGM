import pandas as pd
import re
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


df = pd.read_csv('gradevsvotes.csv')    # pandas dataframe
votes = df['Votes']                     # column of votes without header

votecol = pd.DataFrame(columns=['Votes'])

for vote in votes:
    vote = re.search(r'\d+', vote).group()
    votecol = pd.concat([votecol, pd.DataFrame({'Votes': [int(vote)]})], ignore_index=True)
# print(type(votecol['Votes'].iloc[0]))

df['Votes'] = votecol['Votes']
# print(df.head())

# 设置中文字体
font_path = r'C:\Windows\Fonts\msyhbd.ttc'  # 替换为你的中文字体文件路径
font_prop = fm.FontProperties(fname=font_path)

# 创建图表
plt.figure(figsize=(10, 6))
plt.grid(True)
# 绘制每个数据点并给出标签，用于图例
for i in range(len(df)):
    plt.scatter(df['Votes'][i], df['Grade'][i], label=df['Name'][i])

# 添加标题和标签
plt.title('评分人数 vs 分数', fontsize=14, fontproperties=font_prop)
plt.xlabel('评分人数', fontsize=12, fontproperties=font_prop)
plt.ylabel('分数', fontsize=12, fontproperties=font_prop)

# 显示图例，并设置图例的字体
plt.legend(prop=font_prop, fontsize=1, loc='center left', bbox_to_anchor=(1, 0.5), frameon=False)

# 显示图表
plt.show()