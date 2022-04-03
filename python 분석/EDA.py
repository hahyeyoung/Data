import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
from matplotlib import font_manager,rc

test = pd.read_csv("언급량.csv", encoding = 'UTF-8')
test.head()
test.info()
font_path = 'C:/Windows/Fonts/gulim.ttc'

# 폰트 이름 얻어오기
font_name = font_manager.FontProperties(fname=font_path).get_name()

# 폰트 설정하기
matplotlib.rc('font', family=font_name)

a = test['품목']
b = test['언급량']

xs = [i*3 for i, _ in enumerate(a)]
plt.figure(figsize=(20,10))
plt.bar(xs, b)
plt.xlabel('농작물', fontsize=12)
plt.ylabel('언급량', fontsize=12)
plt.xticks([i*3 for i, _ in enumerate(a)], a)  # x 눈금 및 레이블 설정
plt.title('작물별 키워드 언급량')

ax = test.plot(kind='bar', title='작물별 키워드 언급량', figsize=(12, 4), legend=True, fontsize=12)
ax.set_xlabel('농작물', fontsize=12)          # x축 정보 표시
ax.set_ylabel('언급량', fontsize=12)     # y축 정보 표시
#ax.legend(['언급량'], fontsize=12)    # 범례 지정