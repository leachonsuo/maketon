import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')       #서버에서, 화면에 표시하기 위해서 필요
import seaborn as sns
import altair as alt               ##https://altair-viz.github.io/
import plotly.express as px

st.write("""
# 기온에 따른 범죄율
그래프
""")


# 데이터 불러오기
df = pd.read_csv("wpd_datasets.csv", skiprows=1)  # 첫 줄은 무시
df.columns = ['default_x', 'default_y', 'dataset1_x', 'dataset1_y']  # 열 이름 설정

# Streamlit 앱 제목
st.title("WPD Dataset 시각화")

# 데이터 요약
st.subheader("데이터 미리보기")
st.dataframe(df.head())

# 선 그래프 그리기
st.subheader("기온 선 그래프")
st.line_chart(data=df, x='default_x', y='default_y')

st.subheader("범죄율 선 그래프")
st.line_chart(data=df, x='dataset1_x', y='dataset1_y')

# 두 그래프를 하나의 matplotlib 그래프로 표시
st.subheader("두 데이터셋 비교 (Matplotlib)")
fig, ax = plt.subplots()
ax.plot(df['default_x'], df['default_y'], label='Temperature')
ax.plot(df['dataset1_x'], df['dataset1_y'], label='Number of Crimes')
ax.set_xlabel("Date")
ax.set_ylabel("Two Datasets")
ax.set_title("Compare Two Datasets")
ax.legend()
st.pyplot(fig)

# ----------------------

# 데이터 불러오기
df1 = pd.read_csv("wpd_datasets (2).csv", skiprows=1)  # 첫 줄은 무시
df1.columns = ['default_x', 'default_y', 'dataset1_x', 'dataset1_y']  # 열 이름 설정

# Streamlit 앱 제목
st.title("Temperature 시각화")

# 데이터 요약
st.subheader("데이터 미리보기")
st.dataframe(df1.head())

# 선 그래프 그리기
st.subheader("가중 폭행 그래프")
st.line_chart(data=df1, x='default_x', y='default_y')

st.subheader("기온 그래프")
st.line_chart(data=df1, x='dataset1_x', y='dataset1_y')

# 두 그래프를 하나의 matplotlib 그래프로 표시
st.subheader("두 데이터셋 비교 (Matplotlib)")
fig2, ax2 = plt.subplots()
ax2.plot(df1['default_x'], df1['default_y'], label='Aggravated Assault')
ax2.plot(df1['dataset1_x'], df1['dataset1_y'], label='Temperature')
ax2.set_xlabel("Date")
ax2.set_ylabel("Two Datasets")
ax2.set_title("Compare Two Datasets")
ax2.legend()
st.pyplot(fig2)