import streamlit as st 
import plotly.express as px

st.markdown("""
# Hello
""")


df = px.data.gapminder().query("country=='Canada'")
fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')

st.plotly_chart(fig)