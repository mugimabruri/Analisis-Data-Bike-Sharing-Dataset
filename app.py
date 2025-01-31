# app.py
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Judul Dashboard
st.title('Analisis Data Bike Sharing')

# Load Dataset
df = pd.read_csv('day.csv')

# Mapping nilai musim dan cuaca
season_map = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
weather_map = {1: 'Clear', 2: 'Mist', 3: 'Light Snow/Rain', 4: 'Heavy Rain/Snow'}
df['season'] = df['season'].map(season_map)
df['weathersit'] = df['weathersit'].map(weather_map)

# Sidebar untuk filter data
st.sidebar.header('Filter Data')
selected_season = st.sidebar.selectbox('Pilih Musim', df['season'].unique())
selected_weather = st.sidebar.selectbox('Pilih Cuaca', df['weathersit'].unique())

# Filter data berdasarkan pilihan
filtered_data = df[(df['season'] == selected_season) & (df['weathersit'] == selected_weather)]

# Tampilkan data yang difilter
st.write('Data yang Difilter:')
st.write(filtered_data)

# Visualisasi 1: Pola Penggunaan Sepeda Berdasarkan Musim dan Cuaca
st.header('Pola Penggunaan Sepeda Berdasarkan Musim dan Cuaca')
season_weather_count = df.groupby(['season', 'weathersit'])['cnt'].sum().reset_index()
fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.barplot(x='season', y='cnt', hue='weathersit', data=season_weather_count, ax=ax1)
ax1.set_title('Pola Penggunaan Sepeda Berdasarkan Musim dan Cuaca')
ax1.set_xlabel('Musim')
ax1.set_ylabel('Jumlah Penyewaan Sepeda')
st.pyplot(fig1)

# Visualisasi 2: Hubungan Antara Suhu dan Jumlah Penyewaan Sepeda
st.header('Hubungan Antara Suhu dan Jumlah Penyewaan Sepeda')
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='temp', y='cnt', data=df, ax=ax2)
ax2.set_title('Hubungan Antara Suhu dan Jumlah Penyewaan Sepeda')
ax2.set_xlabel('Suhu (Normalized)')
ax2.set_ylabel('Jumlah Penyewaan Sepeda')
st.pyplot(fig2)