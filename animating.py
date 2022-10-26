import streamlit as st
import pandas as pd
import plotly.express as px

st.title("GDP per Capita over time")
df=px.data.gapminder()
st.write(df)

st.write(df.describe())
year_option=df["year"].unique().tolist()
year=st.selectbox("Select a year:",year_option)
#df=df[df["year"]==year]
fig=px.scatter(df,x="gdpPercap",y="lifeExp",size="pop",color="continent",hover_name="continent",log_x=True,size_max=60, 
                animation_frame="year",animation_group="country",range_x=[100,100000],range_y=[20,90])
fig.update_layout(width=800,height=600)
st.write(fig)