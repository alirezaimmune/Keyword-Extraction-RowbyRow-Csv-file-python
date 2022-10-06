import streamlit as st
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')
st.set_page_config(page_title='The Keyword Extraction App',
    layout='wide')

st.write("""
# 
Hi there!
This Web Application helps you to Extract Keywords from Questions into CSV files.
""")

with st.sidebar.header('1. Upload your CSV data'):
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])


st.subheader('1. Dataset')
global df
if uploaded_file is not None:
    print(uploaded_file)

    try:
        df=pd.read_csv(uploaded_file)
    except Exception as e:
        print(e)
        df=pd.read_csv(uploaded_file)
try:
    st.write(df)
except Exception as e:
    print(e)
    st.write("Waiting to upload file")

st.subheader('2. Keywords')

stop_words = stopwords.words('english')

def get_keywords(row):
    Question = row['Question']
    lowered = Question.lower()
    tokens = nltk.tokenize.word_tokenize(lowered)
    keywords = [keyword for keyword in tokens if keyword.isalpha() and not keyword in stop_words]
    keywords_string = ','.join(keywords)
    return keywords_string
if uploaded_file is not None:
    print(uploaded_file)
    try:
        df['Keywords'] = df.apply(get_keywords, axis=1)
        df
    except Exception as e:
        print(e)
        df=pd.read_csv(uploaded_file)




if uploaded_file is not None:
    print(uploaded_file)
    try:
        st.download_button(label="3.Download the Extracted Keywords",data=df.to_csv(),mime='text/csv')
    except Exception as e:
        print(e)
        df=pd.read_csv(uploaded_file)
