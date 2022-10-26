import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
import plotly.express as px
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

st.markdown(""" 
#**This is a simple EDA app with Streamlit**
# This app performs simple EDA on uploaded CSV data!
# The app is developed by Adeel Munir with help of Codanics youtube channel """)

st.sidebar.header('upload your CSV data')
uploaded_file=st.sidebar.file_uploader("Upload your input CSV file",type=["csv"])
df=sns.load_dataset("titanic")
st.sidebar.markdown("[Example CSV input file](https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv)")

#Prifilling report of Pandas

if uploaded_file is not None:
    def load_csv(): 
        csv=pd.read_csv(uploaded_file)
        return csv
    df=load_csv()
    pr=ProfileReport(df, explorative=True)
    st.header('**Input DataFrame**')
    st.write(df)
    st.write('---')
    st.header('**Profilling report**')
    st_profile_report(pr) 
else:   
    st.info('Awaiting for CSV file to be uploaded.')
    if st.button('Press to use Example Dataset'):
        # Example data
        @st.cache
        def load_data():
            a=pd.DataFrame(
                np.random.rand(100,5),
                columns=['a','b','c','d','e']
            )
            return a
            df=load_data()
            pr=ProfileReport(df, explorative=True)
            st.header('**Input DataFrame**')
            st.write(df)
            st.write('---')
            st.header('**Profilling report**')
            st_profile_report(pr)
