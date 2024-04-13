import streamlit as st
import pandas as pd

st.title('Проект: зарплаты в Data Science')

st.image('scott.jpg', caption='Photo by Scott Graham on https://unsplash.com', width = 600)

st.write('Датасет содержит информацию о зарплатах в Data Science в период с 2020 по 2022 гг.')

df = pd.read_csv('ds_salaries.csv')
df['work_year'] = df['work_year'].astype(str)

st.dataframe(df[['work_year', 'job_title', 'salary_in_usd', 'company_location']])

@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

csv = convert_df(df)

st.write('Данные можно скачать')

st.download_button(
    label="Скачать данные в формате CSV",
    data=csv,
    file_name='ds_salaries.csv',
    mime='text/csv',
)


st.link_button("Источник данных", "https://www.kaggle.com/datasets/zain280/data-science-salaries/data")
